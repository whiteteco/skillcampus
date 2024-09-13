from peewee import SqliteDatabase, Model, IntegerField, CharField, DecimalField

db = SqliteDatabase("peewee_db.sqlite")


class Map(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    location = CharField()
    url = CharField()
    lat = DecimalField()
    lng = DecimalField()
    category = CharField()
    capacity = IntegerField()

    class Meta:
        database = db
        table_name = "map"


db.create_tables([Map])
