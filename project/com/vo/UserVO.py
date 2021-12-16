# Class: CSC-648-848 Fall 2021
# Author: Manali Seth
# Description: Contains columns and datatypes of User Table of database

from wtforms import *

class UserVO:
    userId = IntegerField
    user_loginId = IntegerField
    userName = StringField
