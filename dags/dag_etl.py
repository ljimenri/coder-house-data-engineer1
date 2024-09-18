
import datetime as dt
from airflow import DAG
from airflow.operators.python import PythonOperator
from modules import CreateTableArtists, InsertTableArtists, getToken, favoriteArtists, extractData, extractDataAlbum, joinDataArtistWithAlbum,favoriteAlbum, sendEmailBeginning, sendEmailEnd

with DAG(
        dag_id="artist_etl",
        schedule="@daily",
        catchup=False,
        start_date=dt.datetime(year=2024, month=1, day=30),
        end_date=None,
        tags=["learning", "examples"],
        doc_md="Esto es una dag idempotente"

) as my_dag:
    
    def insert_table(**context):
        InsertTableArtists(joinDataArtistWithAlbum(extractData(getToken(),favoriteArtists()), extractDataAlbum(getToken(),favoriteAlbum())))

    create_table_artists = PythonOperator(
        dag=my_dag,
        task_id="create_table_artists",
        retries=0,
        python_callable=CreateTableArtists
        )
    insert_table_artists = PythonOperator(
        dag=my_dag,
        task_id="insert_table_artists",
        retries=0,
        python_callable=insert_table
        )
    send_email_beginning = PythonOperator(
        dag=my_dag,
        task_id="send_email_beginning",
        retries=0,
        python_callable=sendEmailBeginning,
    )
    send_email_end = PythonOperator(
        dag=my_dag,
        task_id="send_email_end",
        retries=0,
        python_callable=sendEmailEnd,
    )

send_email_beginning >> create_table_artists >> insert_table_artists >> send_email_end
