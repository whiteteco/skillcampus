import pandas as pd
import sqlite3
import os
import logging
from dotenv import load_dotenv
from peewee import Model, IntegerField, CharField, TextField, TimestampField
from playhouse.db_url import connect

load_dotenv(override=True)

# 実行したSQLをログで出力する設定
logger = logging.getLogger("peewee")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

db = connect(os.environ.get("DATABASE"))


class Map(Model):
    """Map Model"""

    id = IntegerField(primary_key=True)  # idは自動で追加されるが明示
    name = CharField()
    lat = IntegerField()
    lng = IntegerField()
    category = CharField()
    capacity = IntegerField()

    class Meta:
        database = db
        table_name = "sc_map"


db.create_tables([Map])
