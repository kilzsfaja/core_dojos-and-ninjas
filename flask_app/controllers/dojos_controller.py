from flask import session, render_template, request, redirect
from flask_app import app
from flask_app.models.dojos_model import Dojo

# ------------------- DISPLAY DOJOS ----------------------
@app.route('/dojos', methods=['GET'])
def display_dojo():
    list_of_dojos = Dojo.display_all_dojos()
    return render_template('index.html', dojos=list_of_dojos)

# -------------------- CREATE DOJO ----------------------
@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    print(request.form)
    data = {
        "name" : request.form["name"]
    }
    Dojo.create_dojo(data)
    return redirect('/dojos')

# -------------------- SHOW ONE DOJO ----------------------

@app.route('/dojos/show/<int:id>', methods=['GET'])
def show_one_dojo_with_ninjas(id):
    data = {
        "id" : id
    }
    dojo = Dojo.get_one_dojo(data)
    return render_template('show_dojo.html', dojo=dojo)