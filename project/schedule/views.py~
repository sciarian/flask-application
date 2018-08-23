############################################################################################
#
# This file is used to store routes used by the web application to display the views
# for the course schedule. 
#
# It can show the address of the page being used for easy readability. Routing is the
# process of mapping URL and HTTP requests to different parts of the web application.
# In terms of MVC, this program maps the user input form the controller to the right 
# views and the views grab necessary data from the model which in this case is html/css docs.
#
# @Author Anthony Sciarini
# @Version 8/15/2018
# @Source http://www.patricksoftwareblog.com/creating-a-simple-flask-web-application/
#         http://www.patricksoftwareblog.com/using-blueprints-to-organize-your-application/
#         http://www.patricksoftwareblog.com/templates-and-bootstrap/
#
############################################################################################

###############
### Imports ###
###############

#Import render_template and Blueprint methods from the flask module
from flask import render_template, Blueprint
from project.models import Course

##############
### Config ###
##############

sr_schedule_blueprint = Blueprint('sr_schedule', __name__, template_folder='templates')
jr_schedule_blueprint = Blueprint('jr_schedule', __name__, template_folder='templates')
sp_schedule_blueprint = Blueprint('sp_schedule', __name__, template_folder='templates')
fr_schedule_blueprint = Blueprint('fr_schedule', __name__, template_folder='templates')

##############
### Routes ###
##############

#This functions goes to the base adress of the main address of the website.
@sr_schedule_blueprint.route('/')
def index():
    #To send html docs in templates dir use "render_template('doc_name.html')"
    #To grab all of the data from the database use ModelName.query.all()
    all_courses = Course.query.all()
    return render_template('sr_schedule.html', courses = all_courses)

#This function will have the route that returns the junior schedule html page 
@jr_schedule_blueprint.route('/jr_schedule')
def jr_sched_index():
    all_courses = Course.query.all()                                 #Query all classes
    return render_template('jr_schedule.html', courses = all_courses)#Return template

#This function will have the route that returns the sophmo schedule html page
@sp_schedule_blueprint.route('/sp_schedule')
def sp_sched_index():
    all_courses = Course.query.all()                                 #Query all classes
    return render_template('sp_schedule.html', courses = all_courses)#Return template

#This function will have the route that returns the freshm schedule html page
@fr_schedule_blueprint.route('/fr_schedule')
def fr_sched_index():
    all_courses = Course.query.all()                                 #Query all classes
    return render_template('fr_schedule.html', courses = all_courses)#Return template
