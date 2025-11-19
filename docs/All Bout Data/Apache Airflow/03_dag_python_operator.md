# DAG menggunakan python operator

> Bogor, 23 Oktober 2025, masuk angkin, ijin kerja tapi tetap belajar....

!!! notes "python operator DAG"


    ```python
        from airflow import DAG # Import DAG
        from datetime import datetime, timedelta
        from airflow.sdk import dag, task, chain


        default_args = {
            'owner' : 'code_farras',
            'retries' : '5',
            'retry_delay' : timedelta(minutes=5)
        }

        @dag(
            description='Learn to create Directed Acyclic Graph python',
            start_date=datetime(2025,10,19), #this part decide when is the DAG run for the 1st time
            schedule= '@daily', # bisa juga menggunakan ekspresi CRON,
            default_args=default_args # Banyak macamnya liat catatan
        )

        def dag_with_python():

            @task
            def script_pertama():
                print("Bismillah")

            @task(task_id="script_renamed")
            def script_nama():
                print("Alhamdulillah")


            chain(script_pertama(),script_nama())
            
        dag_with_python()
    ```

!!! notes "Directed Acylic Graph kode diatas"

    ![alt text](./assets/3_dag_python_ope.png)

