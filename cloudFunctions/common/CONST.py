from os import getenv

SYSTEM_EMAIL = "YOUR SYSTEM E-MAIL ADDRESS"
SYSADMIN = "CONTACT E-MAIL ADDRESS FOR SYSTEM ADMINISTRATOR"
SYSADMIN = f"<a href='{SYSADMIN}'>{SYSADMIN}</a>"

DB_TABLE_NAME = "email_queue"

DB_INSTANCE = [
    "YOUR GCP PROJECT",  # project
    "YOUR GCP DATABASE REGION",  # region
    "YOUR GCP DATABASE INSTANCE NAME",  # instance
]

DB_KWARGS = {
    "drivername": "postgresql+pg8000",
    "username": "YOUR DATABASE USERNAME",
    "database": "YOUR DATABASE NAME",
    "password": getenv("DB_PASSWORD"),
    "query": {"unix_sock": "/cloudsql/{}/.s.PGSQL.5432".format(":".join(DB_INSTANCE))},
}
