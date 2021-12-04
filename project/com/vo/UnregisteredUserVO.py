from wtforms import *

class UnregisteredUserVO:
    sessionId = IntegerField
    name = StringField
    email = StringField
    password = StringField
