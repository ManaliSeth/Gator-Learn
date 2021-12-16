# Class: CSC-648-848 Fall 2021
# Author: Manali Seth
# Description: Contains columns and datatypes of Courses Table of database

from wtforms import *

class CourseVO:
    courseNo = IntegerField
    courseName = StringField
    availability = StringField