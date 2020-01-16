#2naming conventions can choose any
#1. test_circle.py --in this all test modules will be grouped together
#2. circle_test.py  --in this each test module appear next to our test class in our file system
#now lets first create our test case file test_circle.py

#first import unit test module
#now to check circle area function we must import it and also we need to import number pi
# now create a class that is subclass of test case class
#run to check the o/p in GIT bash
#test discoveries one function when we run by cmd
#next we create another class to check if exceptions are raised correctly or not


import unittest
from circle import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # test areas when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

    def test_values(self):
        # Make sure value errors are raised when necessary
        self.assertRaises(ValueError, circle_area, -2)
        #first argument is the exception class that should be raised #2nd argument is a function #and remaining inputs are the arguments to the function

    def test_types(self):
        # Make sure type errors are raised when necessary
        self.assertRaises(TypeError,circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius")




#cd C:/Users/as/PycharmProjects/Giraffe
# python -m unittest   #here it will look for the file to be tested using test discovery method
# - m option instructs Python to run the unit test module as a script

#to get help/details about any function that we want to use lets say assertSetEqual function
# first write # import unittest
#next #help(unittest.TestCase.assertSetEqual)
#this command gives u a detailed description of the function