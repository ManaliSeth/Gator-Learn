
# Class: CSC-648-848 Fall 2021
# Author: Manali Seth, William Yu, Htet Soe, Aarshil Patel, Seela Pant, Christian Robert Samatra
# Description: Contains flask routes to connect and navigate login, registration, about us, home page pages between frontend
#   and backend. Also, contains login for search and other logics

from project import flask_app
from flask import render_template,session, request
from project.com.dao.MajorDAO import MajorDAO
from project.com.dao.CourseDAO import CourseDAO
from project.com.vo.TutorPostingVO import TutorPostingVO
from project.com.dao.TutorPostingDAO import TutorPostingDAO
from project.com.vo.MessageVO import MessageVO
from project.com.dao.MessageDAO import MessageDAO

@flask_app.route('/')
def landingPage():

    majorDAO = MajorDAO()

    # Listing all majors for search bar (All Major dropdown)
    majorDict = majorDAO.viewMajorName()

    courseDAO = CourseDAO()

    # Fetching all courses names for search bar
    courseDict = courseDAO.viewCourseName()

    tutorPostingDAO = TutorPostingDAO()

    # Fetching recent 3 approved tutor postings
    tutorDict = tutorPostingDAO.viewRecentTutorPostings()

    return render_template('user/landingPage.html', majorDict=majorDict, courseDict=courseDict, tutorDict=tutorDict)

@flask_app.route('/userLoadLogin',methods=['GET'])
def userLoadLogin():

    majorDAO = MajorDAO()

    # Listing all majors for search bar (All Major dropdown)
    majorDict = majorDAO.viewMajorName()

    courseDAO = CourseDAO()

    # Fetching all courses names for search bar
    courseDict = courseDAO.viewCourseName()

    return render_template('user/login.html', majorDict=majorDict, courseDict=courseDict)

@flask_app.route('/userLoadRegister',methods=['GET'])
def userLoadRegister():

    majorDAO = MajorDAO()

    # Listing all majors for search bar (All Major dropdown)
    majorDict = majorDAO.viewMajorName()

    courseDAO = CourseDAO()

    # Fetching all courses names for search bar
    courseDict = courseDAO.viewCourseName()

    return render_template('user/registration.html', majorDict=majorDict, courseDict=courseDict)

@flask_app.route('/search',methods=['GET','POST'])
def search():

    majorDAO = MajorDAO()

    # Listing all majors for search bar (All Major dropdown)
    majorDict = majorDAO.viewMajorName()

    courseDAO = CourseDAO()

    # Fetching all courses names for search bar
    courseDict = courseDAO.viewCourseName()

    tutorPostingVO = TutorPostingVO()
    tutorPostingDAO = TutorPostingDAO()

    courses=[]
    for i in courseDict:
        courses.append(i[0])

    search_input = request.form['courseName']

    selectedMajor = request.form['majorDropdown']

    tutorPostingVO.search_input = search_input
    tutorPostingVO.selectedMajor = selectedMajor


    if search_input=='' and selectedMajor=="All Majors":

        # Listing full catalog
        tutorDict, tutorTotalCountDict = tutorPostingDAO.viewTutors()

        tutorTotalCount = []
        for i in tutorTotalCountDict:
            tutorTotalCount.append(i[0])
        tutorTotalCountDict=tutorTotalCount

        if 'loginId' in session:
            return render_template('user/loginSearchResultPage.html', courseDict=courseDict, tutorDict=tutorDict,
                                   tutorTotalCountDict=tutorTotalCountDict, majorDict=majorDict,
                                   search_input=tutorPostingVO.search_input, majorSelected=tutorPostingVO.selectedMajor)
        else:
            return render_template('user/VP_searchResultPage.html', courseDict=courseDict, tutorDict=tutorDict,
                                   tutorTotalCountDict=tutorTotalCountDict, majorDict=majorDict,
                                   search_input=tutorPostingVO.search_input, majorSelected=tutorPostingVO.selectedMajor)


    elif selectedMajor=='All Majors' and search_input != '':

        # Listing particular course tutors
        tutorDict, tutorCountDict = tutorPostingDAO.viewCourseTutors(tutorPostingVO)

        tutorCount = []
        for i in tutorCountDict:
            tutorCount.append(i[0])

        tutorCountDict = tutorCount

        if 'loginId' in session:
            return render_template('user/loginSearchResultPage.html', courseDict=courseDict, tutorDict=tutorDict,
                                   tutorCountDict=tutorCountDict, majorDict=majorDict,
                                   search_input=tutorPostingVO.search_input, majorSelected=tutorPostingVO.selectedMajor)
        else:
            return render_template('user/VP_searchResultPage.html', courseDict=courseDict, tutorDict=tutorDict,
                                   tutorCountDict=tutorCountDict, majorDict=majorDict,
                                   search_input=tutorPostingVO.search_input, majorSelected=tutorPostingVO.selectedMajor)

    elif selectedMajor!='All Majors' and search_input == '':

        # Listing particular Major tutors with no specific course selected
        tutorDict, tutorCountDict, tutorTotalCountDict = tutorPostingDAO.viewMajorTutors(tutorPostingVO)

        tutorCount, tutorTotalCount = [], []
        for i in tutorCountDict:
            tutorCount.append(i[0])

        tutorCountDict = tutorCount

        for i in tutorTotalCountDict:
            tutorTotalCount.append(i[0])
        tutorTotalCountDict = tutorTotalCount

        if 'loginId' in session:
            return render_template('user/loginSearchResultPage.html', courseDict=courseDict, tutorDict=tutorDict,
                                   tutorCountDict=tutorCountDict, tutorTotalCountDict=tutorTotalCountDict,
                                   majorDict=majorDict, search_input=tutorPostingVO.search_input,
                                   majorSelected=tutorPostingVO.selectedMajor)
        else:
            return render_template('user/VP_searchResultPage.html', courseDict=courseDict, tutorDict=tutorDict,
                                   tutorCountDict=tutorCountDict, tutorTotalCountDict=tutorTotalCountDict,
                                   majorDict=majorDict, search_input=tutorPostingVO.search_input,
                                   majorSelected=tutorPostingVO.selectedMajor)


    else:

        # Listing particular major and course tutors
        tutorDict, tutorCountDict, tutorTotalCountDict = tutorPostingDAO.viewMajorCourseTutors(tutorPostingVO)

        tutorCount, tutorTotalCount = [], []
        for i in tutorCountDict:
            tutorCount.append(i[0])

        tutorCountDict = tutorCount

        for i in tutorTotalCountDict:
            tutorTotalCount.append(i[0])
        tutorTotalCountDict = tutorTotalCount

        if 'loginId' in session:
            return render_template('user/loginSearchResultPage.html', courseDict=courseDict, tutorDict=tutorDict,
                               tutorCountDict=tutorCountDict,
                               tutorTotalCountDict=tutorTotalCountDict, majorDict=majorDict,
                               search_input=tutorPostingVO.search_input, majorSelected=tutorPostingVO.selectedMajor)
        else:
            return render_template('user/VP_searchResultPage.html', courseDict=courseDict, tutorDict=tutorDict,
                               tutorCountDict=tutorCountDict,
                               tutorTotalCountDict=tutorTotalCountDict, majorDict=majorDict,
                               search_input=tutorPostingVO.search_input, majorSelected=tutorPostingVO.selectedMajor)


@flask_app.route('/loginLandingPage',methods=['GET','POST'])
def loginLandingPage():

    if 'loginId' in session:

        majorDAO = MajorDAO()

        # Listing all majors for search bar (All Major dropdown)
        majorDict = majorDAO.viewMajorName()

        courseDAO = CourseDAO()

        # Fetching all courses names for search bar
        courseDict = courseDAO.viewCourseName()

        tutorPostingDAO = TutorPostingDAO()

        # Fetching recent 3 approved tutor postings
        tutorDict = tutorPostingDAO.viewRecentTutorPostings()

        messageVO = MessageVO()
        messageDAO = MessageDAO()
        messageVO.msgTo_LoginId = session['loginId']

        # Fetching messages for logged in tutor
        messageDict,messageCountDict = messageDAO.readMessage(messageVO)

        return render_template('user/loginLandingPage.html', majorDict=majorDict, courseDict=courseDict,
                               tutorDict=tutorDict, messageDict=messageDict, messageCountDict=messageCountDict)

@flask_app.route('/aboutUs')
def loadAboutUs():

    majorDAO = MajorDAO()

    # Listing all majors for search bar (All Major dropdown)
    majorDict = majorDAO.viewMajorName()

    courseDAO = CourseDAO()

    # Fetching all courses names for search bar
    courseDict = courseDAO.viewCourseName()

    if 'loginId' in session:
        return render_template('user/loginIndex.html', majorDict=majorDict, courseDict=courseDict)
    else:
        return render_template('user/index.html', majorDict=majorDict, courseDict=courseDict)

@flask_app.route('/loadProfile_AP')
def loadProfile_AP():

    majorDAO = MajorDAO()

    # Listing all majors for search bar (All Major dropdown)
    majorDict = majorDAO.viewMajorName()

    courseDAO = CourseDAO()

    # Fetching all courses names for search bar
    courseDict = courseDAO.viewCourseName()

    if 'loginId' in session:
        return render_template('user/loginIntroduction_Aarshil.html', majorDict=majorDict, courseDict=courseDict)
    else:
        return render_template('user/introduction_Aarshil.html', majorDict=majorDict, courseDict=courseDict)

@flask_app.route('/loadProfile_MS')
def loadProfile_MS():

    majorDAO = MajorDAO()

    # Listing all majors for search bar (All Major dropdown)
    majorDict = majorDAO.viewMajorName()

    courseDAO = CourseDAO()

    # Fetching all courses names for search bar
    courseDict = courseDAO.viewCourseName()

    if 'loginId' in session:
        return render_template('user/loginIntroduction_Manali.html', majorDict=majorDict, courseDict=courseDict)
    else:
        return render_template('user/introduction_Manali.html', majorDict=majorDict, courseDict=courseDict)

@flask_app.route('/loadProfile_HS')
def loadProfile_HS():

    majorDAO = MajorDAO()

    # Listing all majors for search bar (All Major dropdown)
    majorDict = majorDAO.viewMajorName()

    courseDAO = CourseDAO()

    # Fetching all courses names for search bar
    courseDict = courseDAO.viewCourseName()

    if 'loginId' in session:
        return render_template('user/loginIntroduction_Htet.html', majorDict=majorDict, courseDict=courseDict)
    else:
        return render_template('user/introduction_Htet.html', majorDict=majorDict, courseDict=courseDict)

@flask_app.route('/loadProfile_WY')
def loadProfile_WY():

    majorDAO = MajorDAO()

    # Listing all majors for search bar (All Major dropdown)
    majorDict = majorDAO.viewMajorName()

    courseDAO = CourseDAO()

    # Fetching all courses names for search bar
    courseDict = courseDAO.viewCourseName()

    if 'loginId' in session:
        return render_template('user/loginIntroduction_William.html', majorDict=majorDict, courseDict=courseDict)
    else:
        return render_template('user/introduction_William.html', majorDict=majorDict, courseDict=courseDict)

@flask_app.route('/loadProfile_SP')
def loadProfile_SP():

    majorDAO = MajorDAO()

    # Listing all majors for search bar (All Major dropdown)
    majorDict = majorDAO.viewMajorName()

    courseDAO = CourseDAO()

    # Fetching all courses names for search bar
    courseDict = courseDAO.viewCourseName()

    if 'loginId' in session:
        return render_template('user/loginIntroduction_Seela.html', majorDict=majorDict, courseDict=courseDict)
    else:
        return render_template('user/introduction_Seela.html', majorDict=majorDict, courseDict=courseDict)

@flask_app.route('/loadProfile_AM')
def loadProfile_AM():

    majorDAO = MajorDAO()

    # Listing all majors for search bar (All Major dropdown)
    majorDict = majorDAO.viewMajorName()

    courseDAO = CourseDAO()

    # Fetching all courses names for search bar
    courseDict = courseDAO.viewCourseName()

    if 'loginId' in session:
        return render_template('user/loginIntroduction_Aditya.html', majorDict=majorDict, courseDict=courseDict)
    else:
        return render_template('user/introduction_Aditya.html', majorDict=majorDict, courseDict=courseDict)

@flask_app.route('/loadProfile_CR')
def loadProfile_CR():

    majorDAO = MajorDAO()

    # Listing all majors for search bar (All Major dropdown)
    majorDict = majorDAO.viewMajorName()

    courseDAO = CourseDAO()

    # Fetching all courses names for search bar
    courseDict = courseDAO.viewCourseName()

    if 'loginId' in session:
        return render_template('user/loginIntroduction_Christian.html', majorDict=majorDict, courseDict=courseDict)
    else:
        return render_template('user/introduction_Christian.html', majorDict=majorDict, courseDict=courseDict)

# VP_testHomePage for Milestone2

# @flask_app.route('/')
# def HomePage():
#     majorDAO = MajorDAO()
#     majorDict = majorDAO.viewMajorName()
#     courseDAO = CourseDAO()
#     courseDict = courseDAO.viewCourseName()
#     print("MajorDict=",majorDict)
#     print("CourseDict=",courseDict)
#     return render_template('user/VP_testHomePage.html',majorDict=majorDict,courseDict=courseDict)