###
#
# This file is used to show the python interpreter that it is a object and 
# it creates the instance of the flask module (the app variable).
#  
#
###


###############
### imports ###
###############
from flask import Flask

##############
### config ###
##############
app = Flask(__name__)
from . import views
