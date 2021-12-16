# Class: CSC-648-848 Fall 2021
# Author: Manali Seth
# Description: Contains columns and datatypes of Tutor Posting Table of database

from wtforms import *

class TutorPostingVO:
    tpId = IntegerField
    tp_loginId = IntegerField
    tp_majorId = IntegerField
    tp_courseNo = IntegerField
    tutorAvailability = StringField
    tutorDescription = StringField
    tutorCV_datasetName = StringField
    tutorCV_datasetPath = StringField
    tutorAvatar_datasetName = StringField
    tutorAvatar_datasetPath = StringField
    adminApprovalStatus = StringField
