from project import flask_app
from flask import render_template, request
from project.com.vo.CourseVO import CourseVO
from project.com.dao.CourseDAO import CourseDAO


# @flask_app.route('/courseSearch', methods=['GET', 'POST'])
# def courseSearch():
#     if request.method == "GET":
#         courseVO = CourseVO()
#         courseDAO = CourseDAO()
#         courseDict = courseDAO.viewCourseName()
#         print(courseDict)
#         return render_template('viewMajor.html')
#         # book = request.form['book']
#         # search by author or book
#         cursor.execute("SELECT * from Courses ")
#         conn.commit()
#         data = cursor.fetchall()
#
#     return render_template('search.html', data=data)


