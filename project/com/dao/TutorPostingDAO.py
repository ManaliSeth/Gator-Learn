from project import flask_app
# from flask import app
from flaskext.mysql import MySQL

# from project.com.dao import *

mysql = MySQL()
mysql.init_app(flask_app)
conn = mysql.connect()
cursor = conn.cursor()

class TutorPostingDAO:

    def insertTutorPostingDetails(self,tutorPostingVO):

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("Select majorId from Major where majorName='"+str(tutorPostingVO.tutorMajor)+"' ")
        dict1 = cursor.fetchone()
        tp_majorId = str(dict1[0])
        print(tp_majorId)
        tutorPostingVO.tp_majorId = tp_majorId

        cursor.execute("Select courseNo from Courses where courseName='" + str(tutorPostingVO.tutorCourse) + "' ")
        dict1 = cursor.fetchone()
        tp_courseNo = str(dict1[0])
        print(tp_courseNo)
        tutorPostingVO.tp_courseNo = tp_courseNo
        cursor.execute("Insert into TutorPosting(tp_loginId, tp_majorId,tp_courseNo,tutorDescription, tutorCV, tutorAvatar, adminApprovalStatus) values('"+str(tutorPostingVO.tp_loginId)+"', '"+str(tutorPostingVO.tp_majorId)+"', '"+str(tutorPostingVO.tp_courseNo)+"', '"+str(tutorPostingVO.tutorDescription)+"', '"+str(tutorPostingVO.tutorCV)+"', '"+str(tutorPostingVO.tutorAvatar)+"', '"+str(tutorPostingVO.adminApprovalStatus)+"')")

        conn.commit()
        cursor.close()
        conn.close()