from database.createSQL import Book, Song, Author, PublishURL

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///onpuscores.db'
db = SQLAlchemy(app)

# エンジンを作成
engine = create_engine('sqlite:///onpuscores.db')

# セッションを作成
Session = sessionmaker(bind=engine)
session = Session()

import rootes