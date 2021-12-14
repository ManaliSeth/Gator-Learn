from wtforms import *

class TutorPostingVO:
    tpId = IntegerField
    tp_userId = IntegerField
    tp_loginId = IntegerField
    tp_majorId = IntegerField
    tp_courseNo = IntegerField
    tutorAvailability = StringField
    tutorDescription = StringField
    tutorCV = StringField
    tutorAvatar = StringField
    adminApprovalStatus = StringField
