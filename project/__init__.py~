#########################################################################################
#
# This file like any other __init__.py file is used to show the python interpreter 
# that it is a module. In addition to this code is added to create a instace of 
# the flask application and the configuration file used for the instance. This file
# is also used to import all of the views for the program.
#
# @Author Anthony Sciarini
# @Version 8/15/2018
# @Source http://www.patricksoftwareblog.com/creating-a-simple-flask-web-application/
#         http://www.patricksoftwareblog.com/configuring-a-flask-application/
#         https://exploreflask.readthedocs.io/en/latest/blueprints.html#where-do-you-put-them
#
##########################################################################################

###############
### imports ###
###############
from flask import Flask                 #Used to get instance of the flaks application.
from flask_sqlalchemy import SQLAlchemy #Used to connect to database.

##############
### config ###
##############

#Creates a flask application after the name of this module thats instance is relative
#to what secret key is used in the configuration file.

app = Flask(__name__, instance_relative_config=True)
    #Few things to take note of, __name__ refers to the module that the code is
    #being used from.if it is from the source code of the python code being run 
    #then it is the called '__main__'. In this case the flask application is called project.

#Sets the configuration file for the flask application.
app.config.from_pyfile('flask.cfg')
    #Tells the flask application that it should refer to the given file name 
    #(flask.cfg in this case) in the instance_path folder for loading
    #application confurations rather than the root directory of the project.

#Create a db object for the application
db = SQLAlchemy(app)

##################
### Blueprints ###
##################
from project.schedule.views import schedule_blueprint
from project.add_class.views import add_class_blueprint

# register the blueprints
app.register_blueprint(schedule_blueprint)
app.register_blueprint(add_class_blueprint)
