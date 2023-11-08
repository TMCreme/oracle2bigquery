"""
Main module to crawl data from Oracle DB to Bigquery
"""
from typing import List
from google.cloud import bigquery

client = bigquery.Client()

PROJECT_ID = "test_proj"
DATASET = "Staging"
TABLE_NAME = "monikatest"


def create_bigquery_table():
    """Define the schema and create table.
    Assumes that Dataset and project exists"""
    schema = [
        bigquery.SchemaField("id", "INTEGER", mode="REQUIRED"),
        bigquery.SchemaField("first_name", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("last_name", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("email", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("gender", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("location", "STRING", mode="NULLABLE"),
    ]
    table = bigquery.Table(
        f"{PROJECT_ID}.{DATASET}.{TABLE_NAME}", schema=schema
        )
    created_table = client.create_table(table)
    print(
        f"""
        Created table
          {created_table.project}.
          {created_table.dataset_id}.
          {created_table.table_id}"""
        )


def add_data(data_row: List):
    """Add data to the db"""
    sql_query = (
        f"{PROJECT_ID}.{DATASET}.{TABLE_NAME}"
    )
    inserted = client.insert_rows_json(
        sql_query, data_row
    )
    if inserted == []:
        print(f"Successfully inserted a row with id: {data_row[0]['id']}")
    else:
        print("Error encountered: {}".format(inserted))


if __name__ == "__main__":
    create_bigquery_table()
