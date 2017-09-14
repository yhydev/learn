#!/usr/bin/python

from flask import Flask,request,url_for,redirect

app = Flask(__name__)

@app.route("/login")
def login():
	profile = url_for("profile")
	
	return redirect(url_for("profile"))	



@app.route("/index")
def profile():
	print(request.headers)
	return "index";




if __name__ == "__main__":
	app.run(debug = True)
#	app.run()
