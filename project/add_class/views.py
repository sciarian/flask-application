#####################################################################################
#
# This portion of the application is used to route the users URL and HTTP requests 
# to the appropriate views for the "add class"portion of the application where the
# user can add and remove classes to the user schedule.
#
# @Author Anthony Sciarini
# @Version 8/16/2018
# @Source http://www.patricksoftwareblog.com/using-blueprints-to-organize-your-application/
#
#####################################################################################


###############
### Imports ###
###############
from flask import render_template, Blueprint

##############
### Config ###
##############
add_class_blueprint = Blueprint('add_class', __name__, template_folder='templates')

##############
### Routes ###
##############

#TODO Determine route and make html file for the class schedule.
@add_class_blueprint.route('/add_class')
def add_class():
    return render_template('add_class.html')
