from flask_app.models.User import User
from flask_app.controllers import User
from flask_app.models.recipes import Recipe
from flask_app.controllers import recipes
from flask_app import app

if __name__=="__main__":
    app.run(debug=True)

#This should remians simple as this is our root for our application
#Tarot Persona
#the normal password
#double admin