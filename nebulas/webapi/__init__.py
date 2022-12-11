from distutils.command.config import config
from flask import Flask  # Import the Flask class
app = Flask(__name__)    # Create an instance of the class for our use

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

import yaml

from flask_mysqldb import MySQL

######### Enable this for debugging #########
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
SQLALCHEMY_TRACK_MODIFICATIONS = True
######## Enable this for debugging #########

# app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Z4P*i9jjT.e$e]X@localhost/akitaUniverse'
bcrypt = Bcrypt(app)
# app.secret_key = 'random string'

config = yaml.load(open('../config.yaml'), Loader=yaml.Loader)

app.config['MYSQL_HOST'] = config['mysql_host']
app.config['MYSQL_USER'] = config['mysql_user']
app.config['MYSQL_PASSWORD'] = config['mysql_password']
app.config['MYSQL_DB'] = config['mysql_db']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# app.config["MYSQL_CUSTOM_OPTIONS"] = {"ssl": {"ca": "/path/to/ca-file"}}  # https://mysqlclient.readthedocs.io/user_guide.html#functions-and-attributes

# db = SQLAlchemy(app)

mysql = MySQL(app)
# from webapi.db import db
# with app.app_context():
#   db.create_all()
