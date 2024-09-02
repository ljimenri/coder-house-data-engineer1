#!/bin/bash
airflow standalone

airflow db migrate

airflow users create \
    --username admin \
    --firstname luis \
    --lastname jimenez \
    --role Admin \
    --email luisjimenezrivas@gmail.com

airflow webserver --port 8080

airflow scheduler