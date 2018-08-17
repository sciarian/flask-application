############################################################################################
#
# This file is used to store initial routes used by the web application.
# It can show the address of the page being used for easy readability. Routing is the
# process of mapping URL and HTTP requests to different parts of the web application.
# In terms of MVC, this program maps the user input form the controller to the right 
# views and the views grab necessary data from the model which in this case is html/css docs.
#
# @Author Anthony Sciarini
# @Version 8/15/2018
# @Source http://www.patricksoftwareblog.com/creating-a-simple-flask-web-application/
#
############################################################################################

#Import instnce of the flask application
from . import app
from flask import render_template       #Import flask object to render a webpage template.

#This functions goes to the base adress of the main address of the website
@app.route('/')
def index():
    #To send html docs in templates dir use "render_template('doc_name.html')"
    return render_template('base.html')

