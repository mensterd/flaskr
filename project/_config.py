# project/_config.py

import os

# Grab the folder where this script lives
p = os.path.dirname(__file__)
basedir = os.path.abspath(p)


DATABASE = 'db_name.db'
CSRF_ENABLED = True
SECRET_KEY = 'something secret'

# Define full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# The database URI
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH