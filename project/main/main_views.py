# project/main_views.py


# imports ###########################################################

from flask import Flask, Blueprint


# config ############################################################
main_blueprint = Blueprint('mainpage', __name__)





# route handlers ####################################################

@main_blueprint.route('/')
def main():
    return 'This seems to work'