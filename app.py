"""Flask app for adopt app."""

from flask import Flask, render_template, flash, redirect

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get('/')
def show_homepage():
    """List the pets from the database"""

    pets = Pet.query.all()

    return render_template('index.html', title="Adoption Agency", pets=pets)

@app.route("/add", methods = ["GET", "POST"])
def add_pet():
    """Create add pet form and handle data adding """

    form = AddPetForm()

    if form.validate_on_submit():

        pet_name = form.pet_name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age= form.age.data
        notes= form.notes.data

        new_pet = Pet(name=pet_name,
                    species=species,
                    photo_url=photo_url,
                    age=age,
                    notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        flash(f"Successfully added pet: {pet_name}")

        return redirect("/")

    else:
        return render_template("add-pet-form.html", form=form, title="Add Pet!")

@app.route("/<int:pet_id>", methods = ["GET", "POST"])
def edit_pet(pet_id):
    """Edit a pet using their pet id"""

    pet = Pet.query.get(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():

        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        flash(f"Successfully edited pet: {pet.name}")

        return redirect("/")

    else:
        return render_template("display-edit-form.html",
            form=form,
            title=pet.name,
            pet=pet)

