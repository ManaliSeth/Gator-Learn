# Class: CSC-648-848 Fall 2021
# Author: Manali Seth
# Description: Contains columns and datatypes of Messaging Table of database

from wtforms import *

class MessageVO:

    msgId = IntegerField
    msgTo_loginId = IntegerField
    msgFrom_loginId = IntegerField
    msgDate = StringField
    msgTime = StringField
    msgDesc = StringField