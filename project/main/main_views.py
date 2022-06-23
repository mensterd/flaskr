# project/main_views.py


# imports ###########################################################

from flask import Flask, Blueprint, render_template, flash


# config ############################################################
main_blueprint = Blueprint('mainpage', __name__)





# route handlers ####################################################

@main_blueprint.route('/')
def main():
    flash('Hier komen de flasjed messages')
    return render_template('main.html')