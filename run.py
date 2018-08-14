###
# This program runs the flask application. It must be in the top level directory because 
# is calls the package that is made for the flask application in __init__.py file. 
###
DEBUG = True


#Import the flask app from the package we made in project/__init__.py
from project import app

#Run program
if __name__ == "__main__":
    app.run()

