# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///.userDB.sqlite3'
