> Bogor, 08 Desember 2025, bismillah, semoga bisa tinggal dan kerja di Bandung. Aamiin

## How to use ?

Sebelumnya, saya menulis catatan tentang sensor, yang mana kita dapat menggunakan bawaan dari airflow atau dari providers. Catatan kali ini saya menggunakan SFTP sensor yang disediakan oleh providers resmi dari Airflow.

Untuk membuat sensor, yang pertama kali kita butuhkan adalah `connections`. Itu adalah konfigurasi yang dapat saya katakan mirip seperti properties dimana kita menginisasis credentials atau konfigurasi lainnya yang dibutuhkan agar terkoneksi kepada protokol yang dimaksud.

## Create connections

!!! notes "Akses ke connections"

    ![alt text](./assets/08_connecions.png)

!!! notes "Memilih tipe konektor"
    ![alt text](./assets/09_connections_choose.png)


!!! notes "python operator DAG"

    ```python

    import logging

    from airflow import DAG
    from airflow.sdk import chain, task, dag
    from airflow.sdk.bases.sensor import PokeReturnValue
    from datetime import datetime, timedelta
    import logging

    from tornado.process import task_id


    @dag(
        dag_id="SFTP_SENSOR_V3",
        description="Learning SFTP sensor",
        default_args={
            'owner' : 'code_farras',
            'retries' : '5',
            'retry_delay' : timedelta(minutes=5)
        },
        schedule="* * * * *", # Dibuat ulang setiap 5 menit sekali,
        max_active_runs=1 # Agar tidak terjadi over looping
    )
    def my_dag():

        @task.sftp_sensor(
            task_id="wait_for_file",
            sftp_conn_id="laptop_kantor",
            path=f"/airflow/",
            file_pattern="*",
            poke_interval=10,
        )
        def wait_file() -> PokeReturnValue:
            logging.info("File is detected")
            pass

        @task(
            task_id= "prosess_the_file",
        )
        def process_file():
            # Menggunakan SFTP HOOK
            logging.info("RUnn his shit")
            pass
            
        chain(wait_file(), process_file())

    my_dag()
    ```

## Source

* [SFTP Provide](https://airflow.apache.org/docs/apache-airflow-providers-sftp/stable/index.html)