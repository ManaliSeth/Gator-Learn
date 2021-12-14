from project import flask_app
from flask import render_template,session, request, Response, redirect, url_for
from project.com.vo.MajorVO import MajorVO
from project.com.dao.MajorDAO import MajorDAO
from project.com.dao.CourseDAO import CourseDAO
from project.com.vo.TutorPostingVO import TutorPostingVO
from project.com.dao.TutorPostingDAO import TutorPostingDAO
from werkzeug.utils import secure_filename
import os


@flask_app.route('/tutorPosting', methods=['POST'])
def tutorPosting():
    majorDAO = MajorDAO()
    majorDict = majorDAO.viewMajorName()
    courseDAO = CourseDAO()
    courseDict = courseDAO.viewCourseName()
    print("MajorDict=", majorDict)
    print("CourseDict=", courseDict)

    majorVO = MajorVO()

    # selectedMajor = request.form['majorDropdown']
    # majorVO.selectedMajor = selectedMajor

    courseDAO = CourseDAO()
    courseMajorDict = courseDAO.viewCourseMajors(majorVO)
    print(courseMajorDict)

    return render_template('user/tutorPosting.html', majorDict=majorDict, courseDict=courseDict, courseMajorDict=courseMajorDict)


@flask_app.route('/insertTutorPosting', methods=['POST'])
def insertTutorPosting():

    if 'loginId' in session:

        UploadTutorCV_Folder = 'project/static/dataset/tutorCV'
        flask_app.config['UPLOAD_FOLDER'] = UploadTutorCV_Folder
        TutorCV_file = request.files['tutorCV']
        # print(TutorCV_file)
        TutorCV_filename = secure_filename(TutorCV_file.filename)
        # print(TutorCV_filename)
        TutorCV_filepath = os.path.join(flask_app.config['UPLOAD_FOLDER'])
        # print(TutorCV_filepath)
        TutorCV_file.save(os.path.join(flask_app.config['UPLOAD_FOLDER'], TutorCV_filename))

        UploadTutorAvatar_Folder = 'project/static/dataset/tutorAvatar'
        flask_app.config['UPLOAD_FOLDER'] = UploadTutorAvatar_Folder
        TutorAvatar_file = request.files['tutorAvatar']
        # print(TutorAvatar_file)
        TutorAvatar_filename = secure_filename(TutorAvatar_file.filename)
        # print(TutorAvatar_filename)
        TutorAvatar_filepath = os.path.join(flask_app.config['UPLOAD_FOLDER'])
        # print(TutorAvatar_filepath)
        TutorAvatar_file.save(os.path.join(flask_app.config['UPLOAD_FOLDER'], TutorAvatar_filename))

        tp_loginId = session['loginId']
        tutorMajor = request.form['majorDropdown']
        tutorCourse = request.form['courseDropdown']
        tutorDescription = request.form['tutorDescription']

        tutorPostingVO = TutorPostingVO()
        tutorPostingDAO = TutorPostingDAO()

        tutorCV_datasetName = TutorCV_filename
        tutorCV_datasetPath = TutorCV_filepath
        tutorAvatar_datasetName = TutorAvatar_filename
        tutorAvatar_datasetPath = TutorAvatar_filepath

        tutorPostingVO.tp_loginId = tp_loginId
        tutorPostingVO.tutorMajor = tutorMajor
        tutorPostingVO.tutorCourse = tutorCourse
        tutorPostingVO.tutorDescription = tutorDescription
        tutorPostingVO.tutorCV_datasetName = tutorCV_datasetName
        tutorPostingVO.tutorCV_datasetPath = tutorCV_datasetPath
        tutorPostingVO.tutorAvatar_datasetName = tutorAvatar_datasetName
        tutorPostingVO.tutorAvatar_datasetPath = tutorAvatar_datasetPath
        tutorPostingVO.adminApprovalStatus = 'N'

        tutorPostingDAO.insertTutorPostingDetails(tutorPostingVO)

        majorDAO = MajorDAO()
        majorDict = majorDAO.viewMajorName()
        courseDAO = CourseDAO()
        courseDict = courseDAO.viewCourseName()
        # print("MajorDict=", majorDict)
        # print("CourseDict=", courseDict)

        return render_template('user/tutorPosting.html', majorDict=majorDict, courseDict=courseDict)

    else:

        return redirect(url_for('userLoadRegister'))

