"""
Load Postgres module
This script is responsible for loading data into PostgreSQL.
"""
import psycopg2


def get_connection():
    return psycopg2.connect(
        dbname="retail_project",
        user="postgres",
        password="your_password",
        host="localhost",
        port="5432"
    )