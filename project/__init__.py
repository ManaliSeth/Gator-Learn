# Class: CSC-648-848 Fall 2021
# Author: Manali Seth
# Description: Creating flask objects to access routes with it from controller files

from flask import *

flask_app = Flask(__name__)
flask_app.secret_key='abc'

import project.com.controller