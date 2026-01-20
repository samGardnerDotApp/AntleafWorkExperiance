from flask import Flask, render_template, request
import datetime
import csv

def csvToList(path): #Function which converts CSV into a list with each row stored as a list in the list
    values = []
    with open(path, mode ='r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
                #print(lines)
                values.append(lines)
    return values

data = csvToList('moistureData.csv') #Set data variable to contain the CSV data as lists

app = Flask(__name__)

date = datetime.datetime.now() #Sets date variable to current date and time


@app.route("/") #Sets path to this page. e.g. example.com/
def hello_world():
    return render_template("index.html", x=date, rows=int(len(data)), data=data) #Renders the Jinja template and passes data as data, the date as x and the number of rows in the table as rows
