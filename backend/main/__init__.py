from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # Mapping to the database
from flask_cors import CORS
from os import path

db = SQLAlchemy()  # Generate a db instance and bind it to the app
basedir = path.abspath(path.dirname(__file__)) # Get this file path
# db_path = '..\\\\backend\\\\main\\\\test.db'
# sqlalchemy_db_uri = "sqlite:///" + os.path.abspath(db_path)
sqlalchemy_db_uri = 'sqlite:///' + path.join(basedir, 'test.db')

class SingletonApp(object):
    """
    Get the app in singleton mode to ensure that the app is unique throughout the project
    """
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = Flask("COMP9900_Movie_Finder_System")
            CORS(self.instance, supports_credentials=True)
            self.instance.config['DEBUG'] = True
            self.instance.config['SQLALCHEMY_DATABASE_URI'] = sqlalchemy_db_uri
            #self.instance.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # Changes to the database are automatically tracked
            db.init_app(self.instance)  # While initializing the app, bind the app to the DB instance
        return self.instance  # self.instance is the app
