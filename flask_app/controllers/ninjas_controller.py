from flask_app.models.ninjas_model import Ninja
from flask_app.models.dojos_model import Dojo
from flask_app import app
from flask import session, render_template, request, redirect

# ----------------------- NINJA CREATE FORM ------------------
@app.route('/ninjas/form', methods=['GET'])
def ninja_form():
    list_of_dojos = Dojo.display_all_dojos()
    return render_template('new_ninja.html', dojos = list_of_dojos)

# ----------------------- CREATE NINJA ----------------------- 
@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    new_ninja = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    ninja_id = Ninja.create_one_ninja(new_ninja)
    return redirect('/dojos')

# ------------------------ GET ONE NINJA --------------------------
