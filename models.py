"""Models for adopt app."""

from contextlib import nullcontext
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """ Creating a new pet """

    __tablename__ = 'pets'

    id = db.Column(db.Integer,
                primary_key = True,
                autoincrement = True)

    name = db.Column(db.String(50),
                nullable = False)

    species = db.Column(db.String(50),
                nullable = False)

    photo_url = db.Column(db.Text,
                default = "")

    age = db.Column(db.Text,
                nullable = False)

    notes = db.Column(db.Text,
                default = "",
                nullable = False)

    available = db.Column(db.Boolean,
                default = True,
                nullable = False)


