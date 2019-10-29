import csv
with open('C:/Users/Harpreet/Desktop/Bot2.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(row)
