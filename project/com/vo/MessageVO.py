from wtforms import *

class MessageVO:

    msgId = IntegerField
    msgTo_loginId = IntegerField
    msgFrom_loginId = IntegerField
    msgDate = StringField
    msgTime = StringField
    msgDesc = StringField