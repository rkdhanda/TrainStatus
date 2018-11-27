from flask import Flask, redirect, request
import requests
import json
import datetime
import sys
from termcolor import colored
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
now = datetime.datetime.now()


app = Flask(__name__)

def status(trainNo):
	d = now.strftime("%d-%m-%Y")
	api = config['DEFAULT']['API_KEY']
	url = "https://api.railwayapi.com/v2/live/train/"+str(trainNo)+"/date/"+str(d)+"/apikey/"+str(api)
	response = requests.get(url)
	data = response.json()
	train_status = "\nTrain Name : "+colored(data['train']['name'],'red')+"\nStatus : "+colored(data['position'],'red')+"\nCurrent Station : "+colored(data['current_station']['name'],'red')+"\n"
	return train_status

@app.route("/<trainNo>")
def hello(trainNo):
	return status(trainNo)




if __name__ == '__main__':
	app.run(debug=True)
	
