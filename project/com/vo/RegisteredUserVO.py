from wtforms import *

class RegisteredUserVO:
    userId = IntegerField
    sessionId = IntegerField
    majorId = IntegerField
    firstName = StringField
    lastName = StringField
    dateOfBirth = DateField
    gender = StringField
    email = StringField
    password = StringField
    avatar = StringField
    description = StringField
    status = StringField
    role = StringField
