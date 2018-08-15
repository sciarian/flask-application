###########################################################################################
#
# This program runs the flask application. It must be in the top level directory because 
# is calls the package that is made for the flask application in __init__.py file. 
#
# @Author Anthony Sciarini
# @Version 8/15/2018
# @Source http://www.patricksoftwareblog.com/creating-a-simple-flask-web-application/ 
#
###########################################################################################

#Set program to run in debug mode (Maybe be a useless statement do to config file)
DEBUG = True

#Import the flask app from the package we made in project/__init__.py
from project import app

#Run program
if __name__ == "__main__":
    app.run()

