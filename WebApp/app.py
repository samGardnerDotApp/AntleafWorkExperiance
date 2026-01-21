from flask import Flask, render_template, request
import datetime
import csv
from urllib.request import urlretrieve

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTlrhEjK7N8t5rG0kyddsc40PY5xdliOVsMsoMq0Nd-CQ554JfyIcqpHbAHhOfnZvJuSiS3jD7agyEr/pub?gid=0&single=true&output=csv&urp=gmail_link" #URL of where the CSV is stored
filename = "littleJoeSoilMoistureData.csv" #Name to save the retrieved CSV  under

urlretrieve(url, filename) #Downloads the latest Little Joe soil moisture data to the working directory as "littleJoeSoilMoistureData.csv"

def csvToList(path): #Function which converts CSV into a list with each row stored as a list in the list
    values = []
    with open(path, mode ='r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
                #print(lines)
                values.append(lines)
    return values

def graphSafe(data): #Converts the CSV data into a format compatible with graph.js
    graphLabel = []
    graphData = []
    for i in range(len(data)):
        graphLabel.append(data[i][0])
        graphData.append(data[i][1])
    return graphData, graphLabel

data = csvToList('littleJoeSoilMoistureData.csv') #Set data variable to contain the CSV data as lists

data.pop(0)

app = Flask(__name__)

date = datetime.datetime.now() #Sets date variable to current date and time

graphSafeData = graphSafe(data)

@app.route("/") #Sets path to this page. e.g. example.com/
def hello_world():
    return render_template("index.html", x=date, rows=int(len(data)), data=data, graphLabels=graphSafeData[1], graphData=graphSafeData[0]) #Renders the Jinja template and passes data as data, the date as x and the number of rows in the table as rows
