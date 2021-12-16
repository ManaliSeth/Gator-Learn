# Class: CSC-648-848 Fall 2021
# Author: Manali Seth
# Description: Contains queries to insert details and fetch from database

from project import flask_app
from flaskext.mysql import MySQL

mysql = MySQL()
mysql.init_app(flask_app)

class TutorPostingDAO:

    # Inserting tutor posting details into database
    def insertTutorPostingDetails(self,tutorPostingVO):

        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute("Select majorId from Major where majorName='"+str(tutorPostingVO.tutorMajor)+"' ")
        majorId = cursor.fetchone()
        tp_majorId = str(majorId[0])
        tutorPostingVO.tp_majorId = tp_majorId

        cursor.execute("Select courseNo from Courses where courseName='" + str(tutorPostingVO.tutorCourse) + "' ")
        courseNo = cursor.fetchone()
        tp_courseNo = str(courseNo[0])

        tutorPostingVO.tp_courseNo = tp_courseNo
        cursor.execute(
            "Insert into TutorPosting(tp_loginId, tp_majorId,tp_courseNo,tutorDescription, tutorCV_datasetName, tutorCV_datasetPath, tutorAvatar_datasetName, tutorAvatar_datasetPath, adminApprovalStatus) values('" + str(
                tutorPostingVO.tp_loginId) + "', '" + str(tutorPostingVO.tp_majorId) + "', '" + str(
                tutorPostingVO.tp_courseNo) + "', '" + str(tutorPostingVO.tutorDescription) + "', '" + str(
                tutorPostingVO.tutorCV_datasetName) + "', '" + str(tutorPostingVO.tutorCV_datasetPath) + "', '" + str(
                tutorPostingVO.tutorAvatar_datasetName) + "', '" + str(
                tutorPostingVO.tutorAvatar_datasetPath) + "',  '" + str(tutorPostingVO.adminApprovalStatus) + "')")

        conn.commit()
        cursor.close()
        conn.close()

    # Listing full catalog
    def viewTutors(self):

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor2 = conn.cursor()

        cursor.execute(
            "Select * From TutorPosting T, User U, Major M, Courses C WHERE T.adminApprovalStatus='Y' and U.user_loginId=T.tp_loginId and M.majorId=T.tp_majorId and C.courseNo=T.tp_courseNo")
        cursor2.execute("Select count(*) From TutorPosting WHERE adminApprovalStatus='Y'")

        viewTutor = cursor.fetchall()
        viewTutorCount = cursor2.fetchall()

        conn.commit()
        cursor.close()
        conn.close()

        return viewTutor, viewTutorCount

    # Listing particular course tutors
    def viewCourseTutors(self, tutorPostingVO):

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor2 = conn.cursor()

        search_input = "%" + str(tutorPostingVO.search_input) + "%"
        cursor.execute(
            "Select * From TutorPosting T, User U, Major M, Courses C WHERE T.adminApprovalStatus='Y' and C.courseName LIKE '" + search_input + "' and U.user_loginId=T.tp_loginId and M.majorId=T.tp_majorId and C.courseNo=T.tp_courseNo")
        cursor2.execute(
            "Select count(*) From TutorPosting T, User U, Major M, Courses C WHERE T.adminApprovalStatus='Y' and C.courseName LIKE '" + search_input + "' and U.user_loginId=T.tp_loginId and M.majorId=T.tp_majorId and C.courseNo=T.tp_courseNo")

        viewCourseTutor = cursor.fetchall()
        viewCourseTutorCount = cursor2.fetchall()

        conn.commit()
        cursor.close()
        conn.close()

        return viewCourseTutor, viewCourseTutorCount

    # Listing particular Major tutors with no specific course selected
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

        viewTutor = cursor.fetchall()
        viewTutorCount = cursor2.fetchall()
        viewAllTutorCount = cursor3.fetchall()

        conn.commit()
        cursor.close()
        conn.close()

        return viewTutor, viewTutorCount, viewAllTutorCount

    # Listing particular major and course tutors
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

        viewTutor = cursor.fetchall()
        viewTutorCount = cursor2.fetchall()
        viewAllTutorCount = cursor3.fetchall()

        conn.commit()
        cursor.close()
        conn.close()

        return viewTutor, viewTutorCount, viewAllTutorCount

    # Fetching recent 3 approved tutor postings
    def viewRecentTutorPostings(self):

        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT T.*,M.majorName,C.courseName, U.userName FROM TutorPosting T, User U, Major M, Courses C WHERE T.adminApprovalStatus='Y' and U.user_loginId=T.tp_loginId and T.tp_majorId=M.majorId and T.tp_courseNo=C.courseNo ORDER BY T.tpId DESC LIMIT 3")
        recentTutorPosting = cursor.fetchall()

        conn.commit()
        cursor.close()
        conn.close()

        return recentTutorPosting