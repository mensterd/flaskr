# project/api_views.py


# imports ###########################################################

from flask import Flask, Blueprint


# config ############################################################
api_blueprint = Blueprint('api', __name__)





# route handlers ####################################################

@api_blueprint.route('/api/v1/flaskr/<int:some_int_value>')
def api(some_int_value):
    return str(some_int_value)