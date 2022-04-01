from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, URLField, IntegerField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, URL, AnyOf

"""Forms for adopt app."""

AGES = ["baby","young","adult","senior"]

class AddPetForm(FlaskForm):
    """Form to add a new pet """

    pet_name = StringField("Pet Name")
    species = SelectField("Species",
        choices =[("cat","cat"),("dog","dog"),("porcupine","porcupine")],
        validators=[AnyOf(values=["cat","dog","porcupine"])])
    photo_url = URLField("Photo URL", validators=[Optional(),URL()])
    age = SelectField("Age",
        # choices =[("baby","baby"),("young","young"),("adult","adult"),("senior","senior")],
        choices = [(age,age) for age in AGES],
        validators=[AnyOf(AGES)])
    notes = TextAreaField("Notes")

class EditPetForm(FlaskForm):
    """Form to edit an existing pet"""

    photo_url = URLField("Photo URL", validators=[Optional(),URL()])
    notes = TextAreaField("Notes", validators=[Optional()]) #include length validator
    available = BooleanField("Available")
