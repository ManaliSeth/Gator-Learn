# Class: CSC-648-848 Fall 2021
# Author: Manali Seth
# Description: Run this file first to host the Gator learn website

from project import flask_app

if __name__ == "__main__":
	flask_app.debug = True
	flask_app.run(port=8000)
