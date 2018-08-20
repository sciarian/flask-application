##
#
# This program is used to set up the tables for the database for our course schedule
# website. In the flask web development framework and many other web development frame
# works, the term model is used to refer to the tables in the database. So from here
# out I will be using model. Each model will be made with a class that inherits the
# db.Model class. 
# For each db.Model() class... 
#   -A table name will be defined along with a 
#   -Primary key will be defined
#   -Other attributes will be defined as columns
#   -Each column is given a name, datatype, and whether it can have no value or not.
#
# Then a constructor is made to initialize each tuple in the database and then after that
# another function is made to display the representation of each tuple.
#
# @Author Anthony Sciarini
# @Version 8/18/2018
# @Source http://www.patricksoftwareblog.com/database-using-postgresql-and-sqlalchemy/
#
##

###############
### Imports ###
###############
from project import db #Import the databae for this project so we can add to the model

##############
### Models ###
##############
class Course(db.Model):
    
    __tablename__ = "course_table" #Table name

    #########
    #Columns# (Attributes)
    #########
    crn        = db.Column(db.Integer,primary_key=True)
    course     = db.Column(db.String, nullable=False)
    title      = db.Column(db.String, nullable=False)
    campus     = db.Column(db.String, nullable=False)
    credits    = db.Column(db.Float,  nullable=False)
    level      = db.Column(db.String, nullable=False)
    start_date = db.Column(db.String, nullable=False)
    end_date   = db.Column(db.String, nullable=False)
    days       = db.Column(db.String, nullable=False)
    time       = db.Column(db.String, nullable=False)
    location   = db.Column(db.String, nullable=False)
    instructor = db.Column(db.String, nullable=False)
    semester   = db.Column(db.String, nullable=False)

    #############
    #Constructor#
    #############
    def __init__(self, crn, crs, tle, cps, crd, lvl, s_d, e_d, dys, tim, loc, ins, sms):
        self.crn        = crn
        self.course     = crs
        self.title      = tle
        self.campus     = cps
        self.credits    = crd
        self.level      = lvl
        self.start_date = s_d
        self.end_date   = e_d
        self.days       = dys
        self.time       = tim
        self.location   = loc 
        self.instructor = ins
        self.semester   = sms
    
    #Provide a printable format for the application
    def __repr__(self):
        #TODO How do I format the representation??? What does the current string look like?
        return '<TITLE {}'.format(self.name)
