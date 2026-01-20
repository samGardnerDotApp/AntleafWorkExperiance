import csv

def csvToList(path):
    values = []
    with open(path, mode ='r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
                #print(lines)
                values.append(lines)
    return values

print(csvToList('moistureData.csv')[0][1])
