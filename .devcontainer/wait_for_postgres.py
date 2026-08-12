"""Wait for the course database during Codespaces setup."""

import os
import time

import psycopg


connection_parameters = {
    "host": os.environ["PGHOST"],
    "port": os.environ["PGPORT"],
    "dbname": os.environ["PGDATABASE"],
    "user": os.environ["PGUSER"],
    "password": os.environ["PGPASSWORD"],
}

for attempt in range(30):
    try:
        with psycopg.connect(**connection_parameters):
            print("PostgreSQL is ready. Open lab0/Lab0-PostgreSQL-basics.ipynb.")
            break
    except psycopg.OperationalError:
        if attempt == 29:
            raise
        time.sleep(1)
