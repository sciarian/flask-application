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
    #Few things to take note of, __name__ refers to the module that the code is
    #being used from.if it is from the source code of the python code being run 
    #then it is the called '__main__'. In this case the flask application is called project.

#Sets the configuration file for the flask application.
app.config.from_pyfile('flask.cfg')
    #Tells the flask application that it should refer to the given file name 
    #(flask.cfg in this case) in the instance_path folder for loading
    #application confurations rather than the root directory of the project.

#TODO what does this mean???
from . import views
    #This imports everything in the views dir, but why?
