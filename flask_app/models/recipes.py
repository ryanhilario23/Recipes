from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    DB = 'recipes_schema'
    def __init__(self,data):
        self.dish_name = data['dish_name'],
        self.dish_desc = data['dish_desc'],
        self.dish_instrust= data['dish_instrust']
        self.dish_date = data['date'],
        self.cook_time = data['cook_time'],

    @classmethod
    def save_dish(cls,data):
        query = """
                INSERT INTO recipes(name,description,instructions,date,cook_time)
                VALUES (%(dish_name)s,%(dish_desc)s,%(dish_instrust)s,%(date)s,%(cook_time)s);
                """
        print(query)
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    
    @classmethod
    def display_dishes(cls):
        query=  """
                SELECT *
                FROM recipes;
                """
        results = connectToMySQL(cls.DB).query_db(query)
        print(query)
        print(results)
        return results