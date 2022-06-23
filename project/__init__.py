# project/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('_config.py')
db = SQLAlchemy(app)

from project.main.main_views import main_blueprint
from project.api.api_views import api_blueprint


# register blueprint
app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)