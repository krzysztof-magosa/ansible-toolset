from __future__ import absolute_import

from peewee import SqliteDatabase, Model, CharField, TextField, IntegerField


class BaseModel(Model):
    pass

class Vault(BaseModel):
    filename = CharField(unique=True, primary_key=True)
    contents = TextField(null=True)
    mtime = IntegerField(null=True)


def init_models(db):
    models = [
        Vault
    ]

    database = SqliteDatabase(db)

    # wire models with database
    for model in models:
        model._meta.database = database

    database.create_tables(models, safe=True)
