from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, URLField, IntegerField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, URL, AnyOf




"""Forms for adopt app."""



class AddPetForm(FlaskForm):
    """Form to add a new pet """

    pet_name = StringField("Pet Name")
    species = SelectField("Species", choices =[("cat","cat"),("dog","dog"),("porcupine","porcupine")], validators=[AnyOf(values=["cat","dog","porcupine"])])
    photo_url = URLField("Photo URL", validators=[Optional(),URL()])
    age = SelectField("Age", choices =[("baby","baby"),("young","young"),("adult","adult"),("senior","senior")], validators=[AnyOf(["baby","young","adult","senior"])])
    notes = TextAreaField("Notes")

class EditPetForm(FlaskForm):
    """Form to edit an existing pet"""

    photo_url = URLField("Photo URL", validators=[Optional(),URL()])
    notes = TextAreaField("Notes")
    available = BooleanField("Available")
