# Passing parameter

> Bogor, 03 Desember 2025, not feeling well, but learn is a must

`XComs` atau dibaca Cross Communication adalah sebuah mekanisme yang digunakan untuk setiap task saling bertukar data. Pada dasarnya task terisoloasi dan mungkin berjalan dari mesin yang berbeda.

Untuk memanggil data melalui mekanisme tersebut kita harus membuat spesifikias dari mana data tersebut diambil, ada 3 parameter yang dapat kita gunakan untuk mengambil data dari task lain;

1. `key`
2. `task id`
3. `dag id` _jika mengambil dari DAG lain_.

Data yang dikirimkan dapat berupa data tunggal atau ganda, dimana data tersebut bisa bermaca-macam, namun mekanisme tersebut hanya digunakan untuk data dengan besaran yang relative kecil. Maksimal besaran data adalah sebanyak 48kb.

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
        dag_id="XCOM_with_DAG_API",
        description='Learn to create Directed Acyclic Graph python',
        start_date=datetime(2025,10,19), #this part decide when is the DAG run for the 1st time
        schedule= '@daily', # bisa juga menggunakan ekspresi CRON,
        default_args=default_args # Banyak macamnya liat catatan
    )

    def dag_passing_parameter_v1():
        
        @task(do_xcom_push=True, multiple_outputs=True)
        def get_name(**context):
            return {'first_name':'Muhammad Farras',
                    'last_name':'Ma''ruf'}


        @task(do_xcom_push=True, multiple_outputs=True)
        def get_age():
            return {'age':'29'}

        @task
        def script_pertama():
            print("Bismillah")

        @task(task_id="greeting")
        def script_nama(**context):
            print(context)
            data_age = context['ti'].xcom_pull(task_ids="get_age",key="age")
            print(f"Data age: {data_age}")
            # print(f"Data name: {data_name}")

        # Build dependency flow
        first = script_pertama()
        greet = script_nama()

        chain(
            first,
            [get_age(),get_name()] , 
            greet
        )
        
        

    dag_passing_parameter_v1()
    ```

!!! notes "Directed Acylic Graph of above code"

    ![alt text](./assets/5_dag_graph_xcom.png)

Kita dapat meliat data yang dikirim dari setiap task masing-masing

!!! notes "XCOM for each Task"

    ![alt text](./assets/6_dag_xcom_data.png)


## Sources :
* [https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/xcoms.html](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/xcoms.html)
* [Maksimal size XCOM](https://airflow.apache.org/docs/apache-airflow/2.2.2/_modules/airflow/models/xcom.html#MAX_XCOM_SIZE)
* [](https://www.linkedin.com/posts/marclamberti_airflow-apacheairflow-dataengineering-activity-7305982680930611201-fI36/)