"""
Setup information for application. This includes a database connection object and a database config

By: Tom Orth
"""
from app.database.conn import PostgresConnection
import yaml

with open("config.yaml", "r") as f:
    db_config = yaml.load(f, Loader=yaml.FullLoader)
conn = PostgresConnection(db_config)
