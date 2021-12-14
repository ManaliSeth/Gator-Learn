from project import flask_app
from flask import render_template,session, request
from project.com.dao.MajorDAO import MajorDAO
from project.com.dao.CourseDAO import CourseDAO
from project.com.vo.TutorPostingVO import TutorPostingVO
from project.com.dao.TutorPostingDAO import TutorPostingDAO
from flaskext.mysql import MySQL
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
    tutorPostingDAO = TutorPostingDAO()
    tutorDict = tutorPostingDAO.viewRecentTutorPostings()
    print("Tutor Dict=",tutorDict)
    return render_template('user/landingPage.html', majorDict=majorDict, courseDict=courseDict, tutorDict=tutorDict)

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
    courseDict = courseDAO.viewCourseName()
    tutorPostingVO = TutorPostingVO()
    tutorPostingDAO = TutorPostingDAO()
    # registeredUserVO = RegisteredUserVO()
    # registeredUserDAO = RegisteredUserDAO()


    list1=[]
    for i in courseDict:
        list1.append(i[0])
    print(list1)

    search_input = request.form['courseName']
    print("Search input=",search_input)

    selectedMajor = request.form['majorDropdown']
    print("selectedMajor=",selectedMajor)

    tutorPostingVO.search_input = search_input
    tutorPostingVO.selectedMajor = selectedMajor

    # tutorNameDict = tutorPostingDAO.viewTutorName()
    # print(tutorNameDict)

    # registeredUserVO.search_input = search_input
    # registeredUserVO.selectedMajor = selectedMajor

    # Listing full catalog
    if search_input=='' and selectedMajor=="All Majors":
        tutorDict, tutorTotalCountDict = tutorPostingDAO.viewTutors()
        # tutorDict,tutorTotalCountDict = registeredUserDAO.viewTutors()
        print(tutorDict)
        list2 = []
        for i in tutorTotalCountDict:
            list2.append(i[0])
        print(list2)
        tutorTotalCountDict=list2

        return render_template('user/VP_resultPage.html', courseDict=courseDict, tutorDict=tutorDict, tutorTotalCountDict=tutorTotalCountDict, majorDict=majorDict, search_input=tutorPostingVO.search_input, majorSelected=tutorPostingVO.selectedMajor)

    # Listing particular course tutors
    elif selectedMajor=='All Majors' and search_input != '':
        tutorDict, tutorCountDict = tutorPostingDAO.viewCourseTutors(tutorPostingVO)
        # tutorDict,tutorCountDict = registeredUserDAO.viewCourseTutors(registeredUserVO)
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

        return render_template('user/VP_resultPage.html', courseDict=courseDict, tutorDict=tutorDict, tutorCountDict=tutorCountDict, majorDict=majorDict, search_input=tutorPostingVO.search_input, majorSelected=tutorPostingVO.selectedMajor)

    # Listing particular Major tutors with no specific course selected
    elif selectedMajor!='All Majors' and search_input == '':
        tutorDict, tutorCountDict, tutorTotalCountDict = tutorPostingDAO.viewMajorTutors(tutorPostingVO)
        # tutorDict,tutorCountDict, tutorTotalCountDict = registeredUserDAO.viewMajorTutors(registeredUserVO)
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

        return render_template('user/VP_resultPage.html', courseDict=courseDict, tutorDict=tutorDict, tutorCountDict=tutorCountDict, tutorTotalCountDict=tutorTotalCountDict, majorDict=majorDict, search_input=tutorPostingVO.search_input, majorSelected=tutorPostingVO.selectedMajor)

    # Listing particular major and course tutors
    else:
        tutorDict, tutorCountDict, tutorTotalCountDict = tutorPostingDAO.viewMajorCourseTutors(tutorPostingVO)
        # tutorDict, tutorCountDict, tutorTotalCountDict = registeredUserDAO.viewMajorCourseTutors(registeredUserVO)
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

        # return render_template('user/VP_resultPage.html', courseDict=courseDict, tutorDict=tutorDict, tutorCountDict=tutorCountDict,
        #                        tutorTotalCountDict=tutorTotalCountDict, majorDict=majorDict,
        #                        search_input=registeredUserVO.search_input, majorSelected=registeredUserVO.selectedMajor)

        return render_template('user/VP_resultPage.html', courseDict=courseDict, tutorDict=tutorDict,
                               tutorCountDict=tutorCountDict,
                               tutorTotalCountDict=tutorTotalCountDict, majorDict=majorDict,
                               search_input=tutorPostingVO.search_input, majorSelected=tutorPostingVO.selectedMajor)

# @flask_app.route('/viewTutors', methods=['GET'])
# def viewTutors():
#     majorDAO = MajorDAO()
#     majorDict = majorDAO.viewMajorName()
#     registeredUserDAO = RegisteredUserDAO()
#     tutorDict = registeredUserDAO.viewTutors()
#     return render_template('user/VP_resultPage.html',tutorDict=tutorDict, majorDict=majorDict)
#
# @flask_app.route('/_autocomplete', methods=['GET'])
# def autocomplete():
#     courseDAO = CourseDAO()
#     courseDict = courseDAO.viewCourseName()
#     courseName = courseDict[1]
#     print(courseName)
#     return Response(json.dumps(courseName), mimetype='application/json')


@flask_app.route('/loginLandingPage',methods=['GET','POST'])
def loginLandingPage():
    majorDAO = MajorDAO()
    majorDict = majorDAO.viewMajorName()
    courseDAO = CourseDAO()
    courseDict = courseDAO.viewCourseName()
    print("MajorDict=", majorDict)
    print("CourseDict=", courseDict)
    return render_template('user/loginLandingPage.html', majorDict=majorDict, courseDict=courseDict)

@flask_app.route('/aboutUs')
def loadAboutUs():
    majorDAO = MajorDAO()
    majorDict = majorDAO.viewMajorName()
    courseDAO = CourseDAO()
    courseDict = courseDAO.viewCourseName()
    print("MajorDict=", majorDict)
    print("CourseDict=", courseDict)
    if 'loginId' in session:
        return render_template('user/loginIndex.html', majorDict=majorDict, courseDict=courseDict)
    else:
        return render_template('user/index.html', majorDict=majorDict, courseDict=courseDict)

@flask_app.route('/loadProfile_AP')
def loadProfile_AP():
    majorDAO = MajorDAO()
    majorDict = majorDAO.viewMajorName()

    courseDAO = CourseDAO()
    courseDict = courseDAO.viewCourseName()

    print("MajorDict=", majorDict)
    print("CourseDict=", courseDict)

    if 'loginId' in session:
        return render_template('user/loginIntroduction_Aarshil.html', majorDict=majorDict, courseDict=courseDict)
    else:
        return render_template('user/introduction_Aarshil.html', majorDict=majorDict, courseDict=courseDict)

@flask_app.route('/loadProfile_MS')
def loadProfile_MS():
    majorDAO = MajorDAO()
    majorDict = majorDAO.viewMajorName()

    courseDAO = CourseDAO()
    courseDict = courseDAO.viewCourseName()

    print("MajorDict=", majorDict)
    print("CourseDict=", courseDict)

    if 'loginId' in session:
        return render_template('user/loginIntroduction_Manali.html', majorDict=majorDict, courseDict=courseDict)
    else:
        return render_template('user/introduction_Manali.html', majorDict=majorDict, courseDict=courseDict)

@flask_app.route('/loadProfile_HS')
def loadProfile_HS():
    majorDAO = MajorDAO()
    majorDict = majorDAO.viewMajorName()

    courseDAO = CourseDAO()
    courseDict = courseDAO.viewCourseName()

    print("MajorDict=", majorDict)
    print("CourseDict=", courseDict)

    if 'loginId' in session:
        return render_template('user/loginIntroduction_Htet.html', majorDict=majorDict, courseDict=courseDict)
    else:
        return render_template('user/introduction_Htet.html', majorDict=majorDict, courseDict=courseDict)

@flask_app.route('/loadProfile_WY')
def loadProfile_WY():
    majorDAO = MajorDAO()
    majorDict = majorDAO.viewMajorName()

    courseDAO = CourseDAO()
    courseDict = courseDAO.viewCourseName()

    print("MajorDict=", majorDict)
    print("CourseDict=", courseDict)

    if 'loginId' in session:
        return render_template('user/loginIntroduction_William.html', majorDict=majorDict, courseDict=courseDict)
    else:
        return render_template('user/introduction_William.html', majorDict=majorDict, courseDict=courseDict)
@flask_app.route('/loadProfile_SP')
def loadProfile_SP():
    majorDAO = MajorDAO()
    majorDict = majorDAO.viewMajorName()

    courseDAO = CourseDAO()
    courseDict = courseDAO.viewCourseName()

    print("MajorDict=", majorDict)
    print("CourseDict=", courseDict)

    if 'loginId' in session:
        return render_template('user/loginIntroduction_Seela.html', majorDict=majorDict, courseDict=courseDict)
    else:
        return render_template('user/introduction_Seela.html', majorDict=majorDict, courseDict=courseDict)

@flask_app.route('/loadProfile_AM')
def loadProfile_AM():
    majorDAO = MajorDAO()
    majorDict = majorDAO.viewMajorName()

    courseDAO = CourseDAO()
    courseDict = courseDAO.viewCourseName()

    print("MajorDict=", majorDict)
    print("CourseDict=", courseDict)

    if 'loginId' in session:
        return render_template('user/loginIntroduction_Aditya.html', majorDict=majorDict, courseDict=courseDict)
    else:
        return render_template('user/introduction_Aditya.html', majorDict=majorDict, courseDict=courseDict)

@flask_app.route('/loadProfile_CR')
def loadProfile_CR():
    majorDAO = MajorDAO()
    majorDict = majorDAO.viewMajorName()

    courseDAO = CourseDAO()
    courseDict = courseDAO.viewCourseName()

    print("MajorDict=", majorDict)
    print("CourseDict=", courseDict)

    if 'loginId' in session:
        return render_template('user/loginIntroduction_Christian.html', majorDict=majorDict, courseDict=courseDict)
    else:
        return render_template('user/introduction_Christian.html', majorDict=majorDict, courseDict=courseDict)

