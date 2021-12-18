# Class: CSC-648-848 Fall 2021
# Author: Manali Seth
# Description: Contains credentials to connect to SQL Workbench database

from project import *

# Test Database
# flask_app.config['MYSQL_DATABASE_USER'] = 'admin'
# flask_app.config['MYSQL_DATABASE_PASSWORD'] = 'aarshilp'
# flask_app.config['MYSQL_DATABASE_DB'] = 'sfsu-tutoring-app'
# flask_app.config['MYSQL_DATABASE_HOST'] = 'project-1.cxt6ynefb5sw.us-east-2.rds.amazonaws.com'


# Main Database
flask_app.config['MYSQL_DATABASE_USER'] = 'admin'
flask_app.config['MYSQL_DATABASE_PASSWORD'] = 'admin123'
flask_app.config['MYSQL_DATABASE_DB'] = 'se_tutoring'
flask_app.config['MYSQL_DATABASE_HOST'] = 'se-tutoring-database.cxt6ynefb5sw.us-east-2.rds.amazonaws.com'

