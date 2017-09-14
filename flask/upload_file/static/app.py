#!/usr/bin/python

from flask import Flask,request

app = Flask(__name__)

@app.route("/", methods = ["POST"])
def upload():
	upload_file = request.files["file"]

	savePath = "/home/shiyanlou/learn/flask/upload_file/static/"
	filename = upload_file.filename
	abs_filepath = savePath + filename
	upload_file.save(abs_filepath)

	return abs_filepath 

if __name__ == "__main__":
	app.run(debug = True)
#	app.run()
