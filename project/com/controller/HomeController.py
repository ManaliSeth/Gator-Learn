from project import flask_app
from flask import render_template,session, request, Response
from project.com.dao.MajorDAO import MajorDAO
from project.com.dao.CourseDAO import CourseDAO
from project.com.vo.RegisteredUserVO import RegisteredUserVO
from project.com.dao.RegisteredUserDAO import RegisteredUserDAO
from flaskext.mysql import MySQL
import json

mysql = MySQL()
mysql.init_app(flask_app)
conn = mysql.connect()
cursor = conn.cursor()

@flask_app.route('/')
def landingPage():
    # if sessionId in session:
    #     print(session)
    majorDAO = MajorDAO()
    majorDict = majorDAO.viewMajorName()
    courseDAO = CourseDAO()
    courseDict = courseDAO.viewCourseName()
    print("MajorDict=",majorDict)
    print("CourseDict=",courseDict)
    registeredUserDAO = RegisteredUserDAO()
    tutorDict = registeredUserDAO.viewRecentlyAddedTutors()
    print("Tutor Dict=",tutorDict)
    return render_template('user/landingPage.html', majorDict=majorDict, courseDict=courseDict, tutorDict=tutorDict)

@flask_app.route('/aboutUs')
def loadAboutUs():
    return render_template('user/index.html')

# @flask_app.route('/')
# def HomePage():
#     majorDAO = MajorDAO()
#     majorDict = majorDAO.viewMajorName()
#     courseDAO = CourseDAO()
#     courseDict = courseDAO.viewCourseName()
#     print("MajorDict=",majorDict)
#     print("CourseDict=",courseDict)
#     return render_template('user/VP_testHomePage.html',majorDict=majorDict,courseDict=courseDict)

@flask_app.route('/userLoadLogin',methods=['GET'])
def userLoadlogin():
    majorDAO = MajorDAO()
    majorDict = majorDAO.viewMajorName()
    courseDAO = CourseDAO()
    courseDict = courseDAO.viewCourseName()
    print("MajorDict=", majorDict)
    print("CourseDict=", courseDict)
    return render_template('user/login.html', majorDict=majorDict, courseDict=courseDict)

@flask_app.route('/userLoadRegister',methods=['GET'])
def userLoadRegister():
    majorDAO = MajorDAO()
    majorDict = majorDAO.viewMajorName()
    courseDAO = CourseDAO()
    courseDict = courseDAO.viewCourseName()
    print("MajorDict=", majorDict)
    print("CourseDict=", courseDict)
    return render_template('user/registration.html', majorDict=majorDict, courseDict=courseDict)

@flask_app.route('/search',methods=['GET','POST'])
def search():
    majorDAO = MajorDAO()
    majorDict = majorDAO.viewMajorName()
    courseDAO = CourseDAO()
    registeredUserVO = RegisteredUserVO()
    registeredUserDAO = RegisteredUserDAO()
    courseDict = courseDAO.viewCourseName()

    list1=[]
    for i in courseDict:
        list1.append(i[0])
    print(list1)

    search_input = request.form['courseName']
    print("Search input=",search_input)

    selectedMajor = request.form['majorDropdown']
    print("selectedMajor=",selectedMajor)

    registeredUserVO.search_input = search_input
    registeredUserVO.selectedMajor = selectedMajor

    # Listing full catalog
    if search_input=='' and selectedMajor=="All Majors":
        tutorDict,tutorTotalCountDict = registeredUserDAO.viewTutors()
        print(tutorDict)
        list2 = []
        for i in tutorTotalCountDict:
            list2.append(i[0])
        print(list2)
        tutorTotalCountDict=list2

        return render_template('user/VP_resultPage.html', tutorDict=tutorDict, tutorTotalCountDict=tutorTotalCountDict, majorDict=majorDict, search_input=registeredUserVO.search_input, majorSelected=registeredUserVO.selectedMajor)

    # Listing particular course tutors
    elif selectedMajor=='All Majors' and search_input != '':
        tutorDict,tutorCountDict = registeredUserDAO.viewCourseTutors(registeredUserVO)
        print(tutorDict)
        print(tutorCountDict)
        list3, list4 = [], []
        for i in tutorCountDict:
            list3.append(i[0])
        print("list3",list3)
        tutorCountDict = list3

        # for i in tutorTotalCountDict:
        #     list4.append(i[0])
        # print("list4",list4)
        # tutorTotalCountDict = list4

        return render_template('user/VP_resultPage.html', tutorDict=tutorDict, tutorCountDict=tutorCountDict, majorDict=majorDict, search_input=registeredUserVO.search_input, majorSelected=registeredUserVO.selectedMajor)

    # Listing particular Major tutors with no specific course selected
    elif selectedMajor!='All Majors' and search_input == '':
        tutorDict,tutorCountDict, tutorTotalCountDict = registeredUserDAO.viewMajorTutors(registeredUserVO)
        print(tutorDict)
        print(tutorCountDict)
        list3, list4 = [], []
        for i in tutorCountDict:
            list3.append(i[0])
        print("list3",list3)
        tutorCountDict = list3

        for i in tutorTotalCountDict:
            list4.append(i[0])
        print("list4",list4)
        tutorTotalCountDict = list4

        return render_template('user/VP_resultPage.html', tutorDict=tutorDict, tutorCountDict=tutorCountDict, tutorTotalCountDict=tutorTotalCountDict, majorDict=majorDict, search_input=registeredUserVO.search_input, majorSelected=registeredUserVO.selectedMajor)

    # Listing particular major and course tutors
    else:
        tutorDict, tutorCountDict, tutorTotalCountDict = registeredUserDAO.viewMajorCourseTutors(registeredUserVO)
        print(tutorDict)
        print(tutorCountDict)
        list3, list4 = [], []
        for i in tutorCountDict:
            list3.append(i[0])
        print("list3", list3)
        tutorCountDict = list3

        for i in tutorTotalCountDict:
            list4.append(i[0])
        print("list4", list4)
        tutorTotalCountDict = list4

        return render_template('user/VP_resultPage.html', tutorDict=tutorDict, tutorCountDict=tutorCountDict,
                               tutorTotalCountDict=tutorTotalCountDict, majorDict=majorDict,
                               search_input=registeredUserVO.search_input, majorSelected=registeredUserVO.selectedMajor)

@flask_app.route('/viewTutors', methods=['GET'])
def viewTutors():
    majorDAO = MajorDAO()
    majorDict = majorDAO.viewMajorName()
    registeredUserDAO = RegisteredUserDAO()
    tutorDict = registeredUserDAO.viewTutors()
    return render_template('user/VP_resultPage.html',tutorDict=tutorDict, majorDict=majorDict)

@flask_app.route('/_autocomplete', methods=['GET'])
def autocomplete():
    courseDAO = CourseDAO()
    courseDict = courseDAO.viewCourseName()
    courseName = courseDict[1]
    print(courseName)
    return Response(json.dumps(courseName), mimetype='application/json')


@flask_app.route('/loginLandingPage',methods=['GET','POST'])
def loginLandingPage():
    majorDAO = MajorDAO()
    majorDict = majorDAO.viewMajorName()
    courseDAO = CourseDAO()
    courseDict = courseDAO.viewCourseName()
    print("MajorDict=", majorDict)
    print("CourseDict=", courseDict)
    return render_template('user/loginLandingPage.html', majorDict=majorDict, courseDict=courseDict)

@flask_app.route('/tutorPosting')
def tutorPosting():
    majorDAO = MajorDAO()
    majorDict = majorDAO.viewMajorName()
    courseDAO = CourseDAO()
    courseDict = courseDAO.viewCourseName()
    print("MajorDict=", majorDict)
    print("CourseDict=", courseDict)
    return render_template('user/tutorPosting.html', majorDict=majorDict, courseDict=courseDict)

@flask_app.route('/loadProfile_AP')
def loadProfile_AP():
    return render_template('user/introduction_Aarshil.html')

@flask_app.route('/loadProfile_MS')
def loadProfile_MS():
    return render_template('user/introduction_Manali.html')

@flask_app.route('/loadProfile_HS')
def loadProfile_HS():
    return render_template('user/introduction_Htet.html')

@flask_app.route('/loadProfile_WY')
def loadProfile_WY():
    return render_template('user/introduction_William.html')

@flask_app.route('/loadProfile_SP')
def loadProfile_SP():
    return render_template('user/introduction_Seela.html')

@flask_app.route('/loadProfile_AM')
def loadProfile_AM():
    return render_template('user/introduction_Aditya.html')

@flask_app.route('/loadProfile_CR')
def loadProfile_CR():
    return render_template('user/introduction_Christian.html')