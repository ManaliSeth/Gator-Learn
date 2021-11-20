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
    majorDAO = MajorDAO()
    majorDict = majorDAO.viewMajorName()
    courseDAO = CourseDAO()
    courseDict = courseDAO.viewCourseName()
    print("MajorDict=",majorDict)
    print("CourseDict=",courseDict)
    return render_template('user/landingPage.html',majorDict=majorDict,courseDict=courseDict)

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

    selectedMajor = request.form.get('majorSelected')
    print("selectedMajor=",selectedMajor)

    registeredUserVO.search_input = search_input

    if search_input=='':
        tutorDict = registeredUserDAO.viewTutors()
        print(tutorDict)
        return render_template('user/VP_resultPage.html', tutorDict=tutorDict, majorDict=majorDict)

    else:
        tutorDict = registeredUserDAO.viewCourseTutors(registeredUserVO)
        print(tutorDict)
        return render_template('user/VP_resultPage.html', tutorDict=tutorDict, majorDict=majorDict, search_input=registeredUserVO.search_input)

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

@flask_app.route('/login',methods=['GET','POST'])
def login():
    return render_template('user/login.html')

@flask_app.route('/register',methods=['GET','POST'])
def register():
    return render_template('user/registration.html')

@flask_app.route('/userDashboard',methods=['GET','POST'])
def userDashboard():
    return render_template('user/tutorDashboard2.html')

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