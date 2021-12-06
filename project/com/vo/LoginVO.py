from wtforms import *

class LoginVO:
    loginId = IntegerField
    loginEmail = StringField
    loginPassword = StringField
    loginStatus = StringField
