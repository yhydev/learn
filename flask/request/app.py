#!/usr/bin/python

from flask import Flask,request,abort,session

app = Flask(__name__)


#response status setting
@app.route("/abort/<int:status>")
def abort_request(status):
	abort(status)
	return status;


#session set
@app.route("/session/<name>/<value>", methods = ["POST"])
def session_post(name,value):
	session["name"] = value
	return "add success"

#session get
@app.route("/session/<name>", methods = ["GET"])
def session_get(name):
	return session[name]
	
#session delete
@app.route("/session/<name>", methods = ["DELETE"])
def session_delete():
	session.pop(name, None)
	return "delete success"



@app.route("/<name>")
def req():
	eval_str =  ("request.%s" % name)
	print(eval_str)	
	return eval_str


if __name__ == "__main__":
	app.run(debug = True)
#	app.run()
