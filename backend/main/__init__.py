from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # Mapping to the database

db = SQLAlchemy()  # Generate a db instance and bind it to the app

sqlalchemy_db_uri = "sqlite:////test.db"


class SingletonApp(object):
    """
    Get the app in singleton mode to ensure that the app is unique throughout the project
    """
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = Flask("COMP9900_Movie_Finder_System")
            self.instance.config['DEBUG'] = True
            self.instance.config['SQLALCHEMY_DATABASE_URI'] = sqlalchemy_db_uri
            #self.instance.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # Changes to the database are automatically tracked
            db.init_app(self.instance)  # While initializing the app, bind the app to the DB instance
        return self.instance  # self.instance is the app
