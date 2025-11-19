# Membuat DAG, bash operator

> Bogor, 19 Oktober 2025, jam 09:27 PM, malam hari, sudah pada tidur, ngopi, belajar sambil denger kajian radio Rodja bandung, semoga bisa tinggal di bandung, lembang, Aamiin. 

DAG, **Directed** **A**cyclic **G**raph, menggambarkan workflow dengan sturktur yang spesifik.

## Dag Runs

DAG Run adalah sebuah objek yang merepresentasikan sebuah instansi dari DAG. Setiap DAG dapat memiliki skedul atau tidak, yang mana informasi tersebut lah yang membuat DAG berjalan. `schedule_interval` didefinisikan pada argumen DAG itu sendiri dengan menerima `yang paling disarankan` dalam bentuk ekspresi **cron** (String) atau dalam bentuk `#!python datetime.timedelta`. Alternatif laiinya adalah menggunakan salah satu `cron preset` berikut



| preset	| meaning	cron |
| :--- | :--- |
|None	|Don’t schedule, use for exclusively “externally triggered” DAGs|	 
|@once	|Schedule once and only once	 |
|@hourly	|Run once an hour at the beginning of the hour	`0 * * * *`|
|@daily	|Run once a day at midnight	`0 0 * * *`|
|@weekly	|Run once a week at midnight on Sunday morning	`0 0 * * 0`|
|@monthly	|Run once a month at midnight of the first day of the month	`0 0 1 * *`|
|@yearly	|Run once a year at midnight of January 1	`0 0 1 1 *`|

_Note: Use schedule_interval=None and not schedule_interval='None' when you don’t want to schedule your DAG._

`DAG` yang berjalan memiliki kondisi/_state_ (_running_, _failed_, _success_) dan mengingformasikan kepada scheduler tentang rangkaian schedule yang mana yang harus dievaluasi untuk penyerah tugas.

Tanpa adanya metadata pada tingkat DAG run, Airflow scheduler akan memliki banyak kerjaan untuk memahami tugas apa yang harus di triger.

## Default arguments

Saat membuat DAG dan kumpulan task-nya, kita dapat memilih secara eksplisit membarikan kumpulan argumen dari setiap task saat membuat construtor atau ada cara yang lebih baik yaitu menggunakan kumupulan argumen menggunakan default parameter sehingga kita dapat menggunakan berulang dalam membuat task.

!!! notes "Contoh default arguments"

    ```python
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': days_ago(2),
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
        # 'queue': 'bash_queue',
        # 'pool': 'backfill',
        # 'priority_weight': 10,
        # 'end_date': datetime(2016, 1, 1),
        # 'wait_for_downstream': False,
        # 'dag': dag,
        # 'sla': timedelta(hours=2),
        # 'execution_timeout': timedelta(seconds=300),
        # 'on_failure_callback': some_function,
        # 'on_success_callback': some_other_function,
        # 'on_retry_callback': another_function,
        # 'sla_miss_callback': yet_another_function,
        # 'trigger_rule': 'all_success'
    }
    ```

    ```python
        default_args = {
        'owner' : 'code_farras_args',
        'retries' : '5',
        'start_date':datetime(2025,10,27),
        'retry_delay' : timedelta(minutes=5)
    }

    @dag(
        description='Learn to create Directed Acyclic Graph',
        schedule = '@once', # bisa juga menggunakan ekspresi CRON,
        default_args=default_args # Banyak macamnya liat catatan
    )
    ```

## Inisasi Pertama

!!! notes "Inisiasi DAG"

    ```python
    from airflow import DAG # Import DAG
    from datetime import datetime, timedelta


    default_args = {
        'owner' : 'code_farras',
        'retries' : '5',
        'retry_delay' : timedelta(minutes=5)
    }

    with DAG (
        dag_id='dag_pertama',
        description='Learn to create Directed Acyclic Graph',
        start_date=datetime(2025,10,19), #this part decide when is the DAG run for the 1st time
        schedule= '@once', # bisa juga menggunakan ekspresi CRON,
        default_args=default_args # Banyak macamnya liat catatan

    ) as dag:
        pass
    ```

## Create simple task

!!! notes "Membuat task pada DAG"

    ```python
    def dag_pertama():

        @task.bash
        def task_pertama() -> str:
            return "echo Bismillah"    

        task_pertama()


    dag_pertama()
    ```


!!! notes "Graph of Task"

    ![alt text](./assets/4_dag_graph.png)


Dan ketika kita menjalankan Dag serta task tersebut kita dapat melihat hasilnya pada log yang tersedia

!!! note "Log running `dag_pertama`

    ```sh
    [2025-10-23 09:40:48] INFO - DAG bundles loaded: dags-folder
    [2025-10-23 09:40:48] INFO - Filling up the DagBag from /opt/airflow/dags/1_dag_pertama.py
    [2025-10-23 09:40:48] INFO - Tmp dir root location: /tmp
    [2025-10-23 09:40:48] INFO - Running command: ['/usr/bin/bash', '-c', 'echo Bismillah']
    [2025-10-23 09:40:48] INFO - Output:
    [2025-10-23 09:40:48] INFO - Bismillah
    [2025-10-23 09:40:48] INFO - Command exited with return code 0
    ```


## Sumber-sumber

* [Bash Operator](https://airflow.apache.org/docs/apache-airflow-providers-standard/stable/operators/bash.html#skipping)

## Whats next ?
Dag menggunakan python operator, [:material-arrow-right::material-arrow-right::material-arrow-right:](./03_dag_python_operator.md)

