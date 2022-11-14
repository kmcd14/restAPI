from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os 


db=SQLAlchemy()

db_path = os.path.join(os.path.dirname(__file__), 'bookmarks.db')
db_uri = 'sqlite:///{}'.format(db_path)


  # Config database
#app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Creating database tables
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    created = db.Column(db.DateTime, default=datetime.now())
    updated  = db.Column(db.DateTime, onupdate=datetime.now())
    bookmarks = db.relationship('Bookmark', backref='user')


class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=True)
    url = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created = db.Column(db.DateTime, default=datetime.now())
    updated = db.Column(db.DateTime, onupdate=datetime.now())
    visited = db.Column(db.Integer, default=0)