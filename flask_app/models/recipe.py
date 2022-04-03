
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session

# model the class after the table from the database
class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.thirty = data['thirty']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    # Class methods for querying database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('recipes_schema').query_db(query)
        # Create an empty list to append our instances of users
        recipes = []
        # Iterate over the db results and create instances of users with cls.
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes where id=%(id)s;"
        results = connectToMySQL('recipes_schema').query_db(query, data)

        if len(results) < 1:
            return False

        print('Get One Query', results[0])
        return cls(results[0])

    @classmethod
    def save(cls, data):
        print(data)
        query = "INSERT INTO recipes (name, description, instructions, thirty, date_made, created_at, updated_at, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(thirty)s, %(date_made)s, NOW(), NOW(), %(user_id)s);"
        return connectToMySQL('recipes_schema').query_db( query, data )   

    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, thirty=%(thirty)s, date_made=%(date_made)s WHERE id=%(id)s;"
        return connectToMySQL('recipes_schema').query_db( query, data )   

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id=%(id)s"
        return connectToMySQL('recipes_schema').query_db( query, data )   





