# -*- config: utf-8 -*-
from sqlalchemy import create_engine
from application import User, db

create_engine('sqlite:///.userDB.sqlite3')
db.create_all()
