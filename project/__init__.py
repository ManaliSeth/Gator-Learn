from flask import *

flask_app = Flask(__name__)
flask_app.secret_key='abc'

import project.com.controller