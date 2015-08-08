from pony.orm import *
from app import db
from datetime import datetime


class ItemState:
    none = 0
    downloading = 1
    queueing = 2
    downloaded = 3


class Item(db.Entity):
    title = Required(str, unique=True)
    pub_time = Required(datetime, index=True)
    description = Optional(str)
    link = Optional(str)
    category = Optional(str, index=True)
    state = Required(int, index=True, sql_default=0)
    filename = Optional(str)

db.generate_mapping(create_tables=True)