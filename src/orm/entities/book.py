from peewee import *
from .. import database


class Book(Model):
    id = PrimaryKeyField()
    name = CharField()

    class Meta:
        database = database.instance
