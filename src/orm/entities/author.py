from peewee import *
from .. import database


class Author(Model):
    id = PrimaryKeyField()
    firstname = CharField()

    class Meta:
        database = database.instance
