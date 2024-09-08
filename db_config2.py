import logging
import os
from dotenv import load_dotenv
from peewee import Model, IntegerField, CharField, CharField
from playhouse.db_url import connect

load_dotenv(override=True)

# 実行したSQLをログで出力する設定
logger = logging.getLogger("peewee")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

db = connect(os.environ.get("DATABASE"))


class Maker(Model):
    """Maker Model"""

    id = IntegerField(primary_key=True)  # idは自動で追加されるが明示
    category = CharField()
    url = CharField()

    class Meta:
        database = db
        table_name = "sc_maker"


db.create_tables([Maker])
