from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, URLField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, Email, URL, AnyOf




"""Forms for adopt app."""



class AddPetForm(FlaskForm):
    """Form to add a new pet """

    pet_name = StringField("Pet Name")
    species = SelectField("Species", choices =[("c","cat"),("d","dog"),("p","porcupine")], validators=[AnyOf(values=["c","d","p"])])
    photo_url = URLField("Photo URL", validators=[Optional(),URL()])
    age= SelectField("Age", choices =[("baby","baby"),("young","young"),("adult","adult"),("senior","senior")], validators=[AnyOf(["baby","young","adult","senior"])])
    notes= TextAreaField("Notes")
