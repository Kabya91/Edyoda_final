import csv
def showfood():
    with open("./temp.csv", 'r') as file:
        csvreader = csv.reader(file, delimiter=',')
        for row in csvreader:
            print(row)
    
