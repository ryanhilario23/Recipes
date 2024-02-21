from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWOR_REGEX = re.compile(r'a-zA-Z0-9.+_-')

# This is where our queries are made for MYSQL

class User:
    DB = 'prloginnregi_schema'
    def __init__(self,data):
        self.id = data['user_id'],
        self.first_name = data['first_name'],
        self.last_name = data['last_name'],
        self.email = data['email'],
        self.password = data['password'],
        self.passowrd_c = data['password_c']

    @classmethod
    def save_user(cls,data):
        query = """
                INSERT INTO users (first_name, last_name,email,password)
                VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s)
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    
    @classmethod
    def logged_in_user(cls,id):
        query="""
            SELECT *
            FROM users
            WHERE user_id = %(user_id)s
            """
        
        print(query)
        results = connectToMySQL(cls.DB).query_db(query,id)[0]
        print('id',results)
        return results
    
    @classmethod
    def login_email(cls,data):
        if not EMAIL_REGEX.match(data['email']):
                info_valid = False
                return info_valid
        
        query=  """
                SELECT *
                FROM users
                Where email = %(email)s
                """
        print(query)
        results = connectToMySQL(cls.DB).query_db(query,data)
        print('email:', results)
        return results[0]

# Staticmethods
    @staticmethod
    def validate_regi_user(cls):
        info_valid = True
        if len(cls['first_name']) < 3:
            info_valid = False
            flash('First name must be at least three characters long','register')
        
        if len(cls['last_name']) < 3:
            info_valid = False
            flash('Last name must be at least three characters long','register')
        if len(cls['email']) <5:
            info_valid = False
            flash('Email is required.','register')
            if not EMAIL_REGEX.match(cls['email']):
                info_valid = False
                flash('Invlaid email address.','register')
        if len(cls['password']) <8:
            info_valid = False
            flash('Pasword must be at least 8 characters long','register')
        if cls['password'] != cls['password_c']:
            info_valid = False
            flash('Password does not match.','register')
        return info_valid
    

    @staticmethod
    def invalid_account(user):
        if user == False:
            key = False
            flash('Invalid email/password.','login')
            return key
        
    @staticmethod
    def validate_login(cls):
        info_valid= True
        if len(cls['email']) < 3 and len(cls['password'])<3:
            flash('Please insert email and password','login')
            info_valid = False
            return info_valid