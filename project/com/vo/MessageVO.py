from wtforms import *

class MessageVO:

    msgId = IntegerField
    msgTo_userId = IntegerField
    msgFrom_userId = IntegerField
    msgDate = StringField
    msgTime = StringField
    msgDesc = StringField