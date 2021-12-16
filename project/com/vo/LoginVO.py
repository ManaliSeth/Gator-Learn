# Class: CSC-648-848 Fall 2021
# Author: Manali Seth
# Description: Contains columns and datatypes of Login Table of database

from wtforms import *

class LoginVO:
    loginId = IntegerField
    loginEmail = StringField
    loginPassword = StringField
    loginStatus = StringField
