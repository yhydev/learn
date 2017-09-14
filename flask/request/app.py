#!/usr/bin/python

from flask import Flask,request

app = Flask(__name__)

@app.route("/<name>")
def req():
	eval_str =  ("request.%s" % name)
	print(eval_str)	
	return eval_str


if __name__ == "__main__":
	app.run(debug = True)
#	app.run()
