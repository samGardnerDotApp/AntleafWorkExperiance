from flask import Flask, render_template, request
import datetime
import csv
from urllib.request import urlretrieve

debug = False

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTlrhEjK7N8t5rG0kyddsc40PY5xdliOVsMsoMq0Nd-CQ554JfyIcqpHbAHhOfnZvJuSiS3jD7agyEr/pub?gid=0&single=true&output=csv&urp=gmail_link" #URL of where the CSV is stored
filename = "littleJoeSoilMoistureData.csv" #Name to save the retrieved CSV  under

urlretrieve(url, filename) #Downloads the latest Little Joe soil moisture data to the working directory as "littleJoeSoilMoistureData.csv" 

def debugLog(x):
    if debug == True:
        print(f"[DEBUG] {x}")

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

dataStart = 0
dataEnd = 0

graphSafeData = graphSafe(data)

lastUpdated = graphSafeData[1][len(graphSafeData[1])-1]

def setDataRange(start, end):
    if start is None or end is None:
        return start, end

    dataStart = None
    dataEnd = None

    for i, row in enumerate(graphSafeData[1]):
        date_value = str(row)[:10] 

        if str(start) == date_value:
            dataStart = i
        if str(end) == date_value:
            dataEnd = i

        if dataStart is not None and dataEnd is not None:
            break

    return dataStart, dataEnd

def makeDataInRange(start, end, data):
    if start is None or end is None:
        debugLog(f"Values are none returning raw data")
        return data
    debugLog("Values are not none slicing...")
    return data[start:end + 1]

@app.route("/") #Sets path to this page. e.g. example.com/
def main():
    start, end = setDataRange(request.args.get('start'), request.args.get('end'))
    debugLog(f"URL params are: Start: {start}, End: {end}")
    
    return render_template("index.html",  
                           rows=int(len(data)), 
                           data=data, 
                           graphLabels=makeDataInRange(start, end, graphSafeData[1]), 
                           graphData=makeDataInRange(start, end, graphSafeData[0]),
                           lastUpdated=lastUpdated) #Renders the Jinja template and passes data as data and the number of rows in the table as rows