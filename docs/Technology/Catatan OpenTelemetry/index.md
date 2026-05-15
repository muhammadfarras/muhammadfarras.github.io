# Open Telemetry
Observability adalah kemampuan untuk memahami kondisi dalam dari sebuah sistem dengan menganalisa hasil keluaran sistem seperti **logs**, **metrics**, dan **traces**.

* Untuk informasi yang lebih detail, catatan ini hampir sebagiannya bersumber dari [https://spring.io/blog/2025/11/18/opentelemetry-with-spring-boot](https://spring.io/blog/2025/11/18/opentelemetry-with-spring-boot)

## Satu
Dimulai dari Spring Boot 4, OpenTelemetry (otel) memiliki depedency starter, sehingga penggunaanya jauh lebih mudah. Ada 3 depedency yang dibutuhkan.

1. spring-boot-starter-opentelemetry
2. spring-boot-starter-opentelemetry-test
3. opentelemetry-logback-appender-1.0 `for logging`

## Dua
Ada 3 cara untuk menggunakan open telemetry

1. Menggunakan java agent
    * :green_square: mudah dalam penerapannya.
    * :red_square: ada issue jika ada perbedaan versi.
2. Menggunakan third otel starter
    * :red_square: kompleks dalam penerapannya. 
3. Spring boot starter
    * :green_square: easy setup, without possibility issue due to incomptible version, and sedikit perubahan kode.


## Step by Step

### Install depedency

!!! warning
    
    :material-sign-caution::material-sign-caution::material-sign-caution::material-sign-caution:

    Wajib menggunakan Spring boot 4.x.x >

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-opentelemetry</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-webmvc</artifactId>
</dependency>

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-opentelemetry-test</artifactId>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-webmvc-test</artifactId>
    <scope>test</scope>
</dependency>

<dependency>
    <groupId>io.opentelemetry.instrumentation</groupId>
    <artifactId>opentelemetry-logback-appender-1.0</artifactId>
    <version>2.21.0-alpha</version>
</dependency>
```
Yang dibutuhkan sebenarnya hanya 3, namun gua menambahkan Rest untuk testing logging-nya.


### Tambahkan konfigurasi pada application properties

```yml
management:
  tracing:
    sampling:
      probability: 1.0
  otlp:
    metrics:
      export:
        enabled: false
        url: http://localhost:5080/api/vensys/v1/metrics
        headers:
          Authorization: "Basic bWFydWZmYXJyYXNAZ21haWwuY29tOmFkbWlu"
  opentelemetry:
    tracing:
      export:
        otlp:
          endpoint: http://localhost:5080/api/vensys/v1/traces
          headers:
            Authorization: "Basic bWFydWZmYXJyYXNAZ21haWwuY29tOmFkbWlu"
    logging:
      export:
        otlp:
          endpoint: http://localhost:5080/api/vensys/v1/logs
          headers:
            Authorization: "Basic bWFydWZmYXJyYXNAZ21haWwuY29tOmFkbWlu"


server:
  shutdown: immediate
logging:
  level:
    '[ai.ada.mfm]': INFO
    '[org.springframework.boot.actuator.autoconfigure.opentelemetry]': DEBUG
    '[io.opentelemetry.exporter.internal.http]': DEBUG
    '[io.opentelemetry.sdk.trace]': DEBUG
```

Tambahkan konfigurasi diatas. Kalau bingung mengapa menggunakan properties diatas, kita dapat liat di website resmi application properties milik spring boot.

-[https://docs.spring.io/spring-boot/appendix/application-properties/index.html](https://docs.spring.io/spring-boot/appendix/application-properties/index.html)

Kita bisa menggunakan provider lain seperti Grafana, DataDog dan lain-lain. Sehingga spesifikasi endpoint pada URL diatas bisa berbeda-beda. 

- [https://opentelemetry.io/docs/specs/otlp/#otlphttp-request](https://opentelemetry.io/docs/specs/otlp/#otlphttp-request)
- [https://docs.spring.io/spring-boot/reference/actuator/metrics.html#actuator.metrics.export](https://docs.spring.io/spring-boot/reference/actuator/metrics.html#actuator.metrics.export)

### Setup Logging

**OPSIONAL** jika tidak memerulkan store logging maka bagian ini bisa di skip.


Install OpenTelemtry Appender dengan membuat class java

```java
import org.springframework.beans.factory.InitializingBean;
import org.springframework.stereotype.Component;
// import io.opentelemetry;

import io.opentelemetry.api.OpenTelemetry;
import io.opentelemetry.instrumentation.logback.appender.v1_0.OpenTelemetryAppender;

@Component
class InstallOpenTelemetryAppender implements InitializingBean {

    private final OpenTelemetry openTelemetry;

    InstallOpenTelemetryAppender(OpenTelemetry openTelemetry) {
        this.openTelemetry = openTelemetry;
    }

    @Override
    public void afterPropertiesSet() {
        OpenTelemetryAppender.install(this.openTelemetry);
    }
}
```

Buat config XML dengan nama `logback-spring.xml` pada folder `resources`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <include resource="org/springframework/boot/logging/logback/base.xml"/>

    <appender name="OTEL" class="io.opentelemetry.instrumentation.logback.appender.v1_0.OpenTelemetryAppender">
    </appender>

    <root level="INFO">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="OTEL"/>
    </root>
</configuration>
```

### Done
Bagian system yang ingin di observe sudah disetup, selanjutnya observability platforms atau monitoring tools sebagai pusat informasi kondisi sistem. Gua mengunakan **OpenObserver**.

### Setup dan jalankan OpenObserver
Gua pakai docker untuk membuat container openobserver.

```yml
services:
  openobserve:
    image: o2cr.ai/openobserve/openobserve-enterprise:latest
    container_name: openobserve
    environment:
      - ZO_ROOT_USER_EMAIL=maruffarras@gmail.com
      - ZO_ROOT_USER_PASSWORD=admin
      - ZO_DATA_DIR=/data
    ports:
      - "5080:5080"
    volumes:
      - oo_data:/data
volumes:
  oo_data: {}
```

Jalankan perintah `docker compose up -d`

### Jalankan springboot

Jalankan spring dengan `mvn spring-boot:run`

Lalu hit endpoint

```http
GET http://localhost:8080
```


### Done all
Alhamdulillah, berikut catatan ringkas semoga bisa digunakan dan diimplementasi. Kita juga dapat membuat alert system jika terjadi error pada sistem dengan memberikan notifikasi misalnya ke Discord atau platform lainnya. Coba eksplore lebih lanjut masing-masing observeability platforms.