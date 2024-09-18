
import datetime as dt
from airflow import DAG
from airflow.operators.python import PythonOperator
from modules import CreateTableArtists, InsertTableArtists, getToken, callApi, getAlbumAPI, favoriteArtists, extractData, extractDataAlbum, joinDataArtistWithAlbum,favoriteAlbum, sendEmail

with DAG(
        dag_id="artist_etl",
        schedule="@daily",
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
        python_callable=CreateTableArtists
        )
    insert_table_artists = PythonOperator(
        dag=my_dag,
        task_id="insert_table_artists",
        python_callable=insert_table
        )

create_table_artists >> insert_table_artists >> send_email
