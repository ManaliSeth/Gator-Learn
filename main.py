from project import flask_app

if __name__ == "__main__":
	flask_app.debug = True
	flask_app.run(port=8000)
