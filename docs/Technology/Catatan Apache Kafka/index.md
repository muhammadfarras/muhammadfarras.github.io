# Strkutr
Producer -> Broker -> Topic -> Partition

## Kafka topics
Topics : particular stream of data
* Seperti tabel pada databases
* Dapat memliki opik yang banyak
* Topik teridentifikasi dengan _name_
* Dapat berisi format apapun, JSON, XML dsb
* Kumpulan message disetbut dengan _data stream_
* Tidak dapat langusng query topics, gunakan **Kafka Producers** untuk menbaca dan mengirim data
asd
Misal

Terisi dari 
0 logs
0 Purchases
0 Twitter Tweets
0 truck_gps

### Partisi dan Offserts
Topic dipecah dalam bentuk partisi. Message yang ada didalam partisi tersusun berurut.
Setiap message didalam partisi memliki id, yang disebut offset.

* Kafka topic immutable, tidak dapat dirubah.
* Data disimpan sementara, bawaanya selama 7 hari (retention)
* Data terurut hanya dijamin didalam topics, tidak dengan cross topics
* Dapat memliki lebih dari satu partition didalam satu topic
* Data di set secara acak kdalam partition kecuaili key is porvided (offset kah ?)


## Producers
Producers write dat aain topic



### Membuat topic
```shell
kafka-topics.sh --bootstrap-server localhost:9092 --topic topic_A --create
```

```shell
kafka-topics.sh --bootstrap-server localhost:9092 --topic topic_B --create --partitions 3
```

```shell
kafka-topics.sh --bootstrap-server localhost:9092 --topic topic_C --create --partitions 3 --replication-factor 2 #(1)!

kafka-topics.sh --bootstrap-server localhost:9092 --topic topic_C --create --partitions 3 --replication-factor 1 #(2)!
```

1.  Due error, karena hanya memliki satu buah broker
2.  Tidak error

Melihat informasi semua topics
```shell
kafka-topics.sh --bootstrap-server localhost:9092 --topic topic_A --describe
```

Untuk melihat informasi dari topics tertentu
```shell
kafka-topics.sh --bootstrap-server localhost:9092 --topic topic_A --describe #(1)!
```

### Menahpus topic

```shell
# Menghapus topic C
kafka-topics.sh --bootstrap-sever localhost:9092 --topic topic_B --delete
```



### Kafka console producer
Untuk mengirimkan message ataupun producer
```shell
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic topic_C
```

Menggunakan producer property
!!! info
    --producer-property <String:producer_prop> A mechanism to pass user-defined properties in the form key=value to the producer.
  
```shell
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic topic_C --producer-property acks=1  
```