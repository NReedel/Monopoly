###############################################################
# app.py
# flask app for monopoly-game
###############################################################

from static.py.monopoly import *
from flask import Flask, render_template
import os

###############################################################

# switch T/F to run monopoly or flask
# cannot run both yet!
run_monopoly = True
run_flask = False

if run_monopoly:
	monopoly = Monopoly()
	running = True
	while running == True:
		running = monopoly.run()

###############################################################

if run_flask:
	app = Flask(__name__)

	@app.route("/")
	def hello_world():
		return render_template('monopoly.html', title='Monopoly Game') # monopoly=monopoly

###############################################################