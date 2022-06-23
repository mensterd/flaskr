# project/api_views.py


# imports ###########################################################

from flask import Flask, Blueprint


# config ############################################################
api_blueprint = Blueprint('api', __name__)





# route handlers ####################################################

@api_blueprint.route('/api/')
def main():
    return 'api'