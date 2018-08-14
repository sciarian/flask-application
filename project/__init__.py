###
#
# This file is used to show the python interpreter that it is a object and 
# it creates the instance of the flask module (the app variable).
#
###


###############
### imports ###
###############
from flask import Flask

##############
### config ###
##############

#Creates a flask application after the name of this module thats instance is relative
#to what secret key is used in the configuration file.

app = Flask(__name__, instance_relative_config=True)
    #Few things to take note of, __name__ refers to the module that the code is being used from.
    #if it is from the source code of the python code being run then it is the called '__main__'

app.config.from_pyfile('flask.cfg')

from . import views

