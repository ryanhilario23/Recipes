from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.recipes import Recipe
from flask_app.controllers.User import User
from flask import flash

@app.route('/create_dish')
def create_dish():
    return render_template('/create.html')

@app.route('/create_dish/push', methods=['POST'])
def saving_dish():
    # Have to check the form is filled

    form = request.form
    data = {
        'dish_name': form['dish_name'],
        'dish_desc': form['dish_desc'],
        'dish_instrust': form['dish_instrust'],
        'date': form['date'],
        'cook_time': form['cook_time']
    }
    print(data)
    dish_id = Recipe.save_dish(data)
    session['dish_id'] = dish_id
    return redirect('/dashboard')