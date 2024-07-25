from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        #Gets the note from the HTML
        note = request.form.get('note')

        if len(str(note)) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id) # providing the schema for the note
            db.session.add(new_note) # adding the note to the database 
            db.session.commit()
            flash('Note added.', category='success')

    return render_template("home.html", user=current_user)