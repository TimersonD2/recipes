
from flask import render_template, request, redirect, flash, session
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_app import app


@app.route("/addRecipe")
def addRecipe():
    return render_template("createRecipe.html")

@app.route('/createRecipe', methods=["POST"])
def createRecipe():
#     # First we make a data dictionary from our request.form coming from our template.
#     # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "name": request.form["name"],
        "description" : request.form["description"],
        "instructions" : request.form["instructions"],
        "thirty" : request.form['thirty'],
        "date_made" : request.form["date_made"],
        "user_id" : session["user_id"]
    }
    # We pass the data dictionary into the save method from the User class.
    print(data)
    recipe_id = Recipe.save(data)
    session['recipe_id'] = recipe_id
    return redirect('/success/')

@app.route('/showRecipe/<int:recipe_id>/show')
def showRecipe(recipe_id):
    data = {
        "id": recipe_id
    }
    return render_template("showRecipe.html", one_recipe=Recipe.get_one(data))

@app.route('/editRecipe/<int:recipe_id>/edit')
def editRecipe(recipe_id):
    data = {
        "id": recipe_id
    }
    return render_template("editRecipe.html", one_recipe=Recipe.get_one(data))

@app.route('/updateRecipe/<int:recipe_id>/update', methods=["POST"])
def updateRecipe(recipe_id):
    data = {
        "id": recipe_id,
        "name": request.form["name"],
        "description" : request.form["description"],
        "instructions" : request.form["instructions"],
        "thirty" : request.form["thirty"],
        "date_made" : request.form["date_made"],
        "creator" : session["user_id"]
    }
    Recipe.update(data)
    return redirect('/success/')
    # return redirect('/')


@app.route('/deleteRecipe/<int:recipe_id>/delete')
def deleteRecipe(recipe_id):
    data = {
        "id": recipe_id
    }
    Recipe.delete(data)
    return redirect("/success/")


