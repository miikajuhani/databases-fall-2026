"""Reset only the table used in Lab 0."""

from pathlib import Path
import os

import psycopg


with psycopg.connect(
    host=os.environ["PGHOST"],
    port=os.environ["PGPORT"],
    dbname=os.environ["PGDATABASE"],
    user=os.environ["PGUSER"],
    password=os.environ["PGPASSWORD"],
    autocommit=True,
) as connection:
    with connection.cursor() as cursor:
        cursor.execute(Path(__file__).with_name("reset-lab0.sql").read_text())

print("Lab 0 has been reset. Return to the notebook and run its reset cell.")
