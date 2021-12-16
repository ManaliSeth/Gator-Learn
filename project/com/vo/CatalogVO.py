# Class: CSC-648-848 Fall 2021
# Author: Manali Seth
# Description: Contains columns and datatypes of Catalog Table of database

from wtforms import *

class CatalogVO:
    majorId = IntegerField
    courseNo = IntegerField
    requirement = StringField
