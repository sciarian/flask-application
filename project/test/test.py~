###
#
# This prorgam is will contain all of the unit tests to test our application.
# 
# ***To run unit tests for this project head to the top level and use command 'nose2'
#    this will automatically find and run the units tests for this project.
#
# *To run a regular unit test use the command 'python unit_test.ut.py -v'. 
#
###

#############
### Libs ####
#############

import unittest             #Library for unit testing.
from project import app     #Import the flask application instance for this project.

#Unit test guidelines.
#   -the directory containg the test cases should be named 'test'
#   -all unit test should be in the format 'test_*.py'
#    this is so the nose2 package can find the unit tests for us.


class ProjectTests(unittest.TestCase):

    ############################
    ### Set Up and Tear Down ###
    ############################
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

        self.assertEquals(app.debug, False)

    def tearDown(self):
        pass

    ########################
    ### Helper functions ###
    ########################

    #TODO TBD

    #############
    ### Tests ###
    #############

    #Simple unit test used to test how to use unit tests
    def test_unit_test(self):
        print("Unit tests are functioning properly")
        self.assertTrue(True)


#Run Program
if __name__ == '__main__':
    unittest.main()
