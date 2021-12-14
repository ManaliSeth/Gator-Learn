from project import flask_app
# from flask import app
from flaskext.mysql import MySQL



# from project.com.dao import *

mysql = MySQL()
mysql.init_app(flask_app)
# conn = mysql.connect()
# cursor = conn.cursor()

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
        cursor.execute("Insert into TutorPosting(tp_loginId, tp_majorId,tp_courseNo,tutorDescription, tutorCV_datasetName, tutorCV_datasetPath, tutorAvatar_datasetName, tutorAvatar_datasetPath, adminApprovalStatus) values('"+str(tutorPostingVO.tp_loginId)+"', '"+str(tutorPostingVO.tp_majorId)+"', '"+str(tutorPostingVO.tp_courseNo)+"', '"+str(tutorPostingVO.tutorDescription)+"', '"+str(tutorPostingVO.tutorCV_datasetName)+"', '"+str(tutorPostingVO.tutorCV_datasetPath)+"', '"+str(tutorPostingVO.tutorAvatar_datasetName)+"', '"+str(tutorPostingVO.tutorAvatar_datasetPath)+"',  '"+str(tutorPostingVO.adminApprovalStatus)+"')")

        conn.commit()
        cursor.close()
        conn.close()

    # def viewTutorName(self):
    #
    #     conn = mysql.connect()
    #     cursor = conn.cursor()
    #
    #     cursor.execute("Select userName from User U, TutorPosting T where U.user_loginId = T.tp_loginId and T.adminApprovalStatus='Y'")
    #     tutorNameDict = cursor.fetchall()
    #     conn.commit()
    #     cursor.close()
    #     conn.close()
    #
    #     return tutorNameDict

    def viewTutors(self):

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor2 = conn.cursor()

        cursor.execute("Select * From TutorPosting T, User U, Major M, Courses C WHERE T.adminApprovalStatus='Y' and U.user_loginId=T.tp_loginId and M.majorId=T.tp_majorId and C.courseNo=T.tp_courseNo")
        cursor2.execute("Select count(*) From TutorPosting WHERE adminApprovalStatus='Y'")
        dict1 = cursor.fetchall()
        dict2 = cursor2.fetchall()

        conn.commit()
        cursor.close()
        conn.close()

        return dict1, dict2

    def viewCourseTutors(self, tutorPostingVO):

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor2 = conn.cursor()

        search_input = "%" + str(tutorPostingVO.search_input) + "%"
        cursor.execute("Select * From TutorPosting T, User U, Major M, Courses C WHERE T.adminApprovalStatus='Y' and C.courseName LIKE '" + search_input + "' and U.user_loginId=T.tp_loginId and M.majorId=T.tp_majorId and C.courseNo=T.tp_courseNo")
        cursor2.execute("Select count(*) From TutorPosting T, User U, Major M, Courses C WHERE T.adminApprovalStatus='Y' and C.courseName LIKE '" + search_input + "' and U.user_loginId=T.tp_loginId and M.majorId=T.tp_majorId and C.courseNo=T.tp_courseNo")
        # cursor3.execute("Select count(*) From RegisteredUser WHERE role='Tutor'")
        dict1 = cursor.fetchall()
        dict2 = cursor2.fetchall()
        # dict3 = cursor3.fetchall()

        conn.commit()
        cursor.close()
        conn.close()

        return dict1, dict2

    def viewMajorTutors(self, tutorPostingVO):

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor2 = conn.cursor()
        cursor3 = conn.cursor()

        cursor.execute(
            "Select * From TutorPosting T, User U, Major M, Courses C  WHERE T.adminApprovalStatus='Y' and M.majorId in (Select majorId from Major where majorName ='" + tutorPostingVO.selectedMajor + "') and U.user_loginId=T.tp_loginId and M.majorId=T.tp_majorId and C.courseNo=T.tp_courseNo")
        cursor2.execute(
            "Select count(*) From TutorPosting T, User U, Major M, Courses C WHERE T.adminApprovalStatus='Y' and M.majorId in (Select majorId from Major where majorName ='" + tutorPostingVO.selectedMajor + "') and U.user_loginId=T.tp_loginId and M.majorId=T.tp_majorId and C.courseNo=T.tp_courseNo")
        cursor3.execute("Select count(*) From TutorPosting WHERE adminApprovalStatus='Y'")
        dict1 = cursor.fetchall()
        dict2 = cursor2.fetchall()
        dict3 = cursor3.fetchall()

        conn.commit()
        cursor.close()
        conn.close()

        return dict1, dict2, dict3

    def viewMajorCourseTutors(self, tutorPostingVO):

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor2 = conn.cursor()
        cursor3 = conn.cursor()

        search_input = "%" + str(tutorPostingVO.search_input) + "%"
        cursor.execute(
            "Select * From TutorPosting T, User U, Major M, Courses C WHERE T.adminApprovalStatus='Y' and C.courseName LIKE '" + search_input + "' and M.majorId in (Select majorId from Major where majorName ='" + tutorPostingVO.selectedMajor + "') and U.user_loginId=T.tp_loginId and M.majorId=T.tp_majorId and C.courseNo=T.tp_courseNo")
        cursor2.execute(
            "Select count(*) From TutorPosting T, User U, Major M, Courses C WHERE T.adminApprovalStatus='Y' and courseName LIKE '" + search_input + "' and M.majorId in (Select majorId from Major where majorName ='" + tutorPostingVO.selectedMajor + "') and U.user_loginId=T.tp_loginId and M.majorId=T.tp_majorId and C.courseNo=T.tp_courseNo")
        cursor3.execute("Select count(*) From TutorPosting WHERE adminApprovalStatus='Y'")
        dict1 = cursor.fetchall()
        dict2 = cursor2.fetchall()
        dict3 = cursor3.fetchall()

        conn.commit()
        cursor.close()
        conn.close()

        return dict1, dict2, dict3

    def viewRecentTutorPostings(self):

        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM TutorPosting T, User U, Major M, Courses C WHERE T.adminApprovalStatus='Y' and U.user_loginId=T.tpId ORDER BY tpId DESC LIMIT 3;")
        dict1 = cursor.fetchall()

        conn.commit()
        cursor.close()
        conn.close()

        return dict1