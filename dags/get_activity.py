"""
get_activity
DAG auto-generated by Astro Cloud IDE.
"""

from airflow.decorators import dag
from astro import sql as aql
import pandas as pd
import pendulum


@aql.dataframe(task_id="fetch_activity")
def fetch_activity_func():
    return

default_args={
    "owner": "Cristian Yeraldo Urcuqui Ortega,Open in Cloud IDE",
}

@dag(
    default_args=default_args,
    schedule="0 0 * * *",
    start_date=pendulum.from_format("2024-09-10", "YYYY-MM-DD").in_tz("UTC"),
    catchup=False,
    owner_links={
        "Cristian Yeraldo Urcuqui Ortega": "mailto:cristianurcuqui@gmail.com",
        "Open in Cloud IDE": "https://cloud.astronomer.io/cm0vt052100vf01nel4wlj39y/cloud-ide/cm0vtdir200x601nebqxwfkp4/cm0vtdw7o00xb01nefmfvpt1n",
    },
)
def get_activity():
    fetch_activity = fetch_activity_func()

dag_obj = get_activity()
