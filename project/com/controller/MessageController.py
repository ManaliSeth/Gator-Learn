from project import flask_app
from flask import render_template,session, request, Response
from project.com.dao.MajorDAO import MajorDAO
from project.com.dao.CourseDAO import CourseDAO
from project.com.vo.RegisteredUserVO import RegisteredUserVO
from project.com.dao.RegisteredUserDAO import RegisteredUserDAO
from project.com.vo.UnregisteredUserVO import UnregisteredUserVO
from project.com.dao.UnregisteredUserDAO import UnregisteredUserDAO
from flaskext.mysql import MySQL
import json

@flask_app.route('/searchData',methods=['POST'])
def searchData():
    pass