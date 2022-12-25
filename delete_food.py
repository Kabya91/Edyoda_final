import csv

with open('temp.csv', 'r') as f:
    reader = csv.reader(f)
    with open('output.csv', 'w') as f1:
        writer = csv.writer(f1)
        for row in reader:
            if row[0] != '1':
                writer.writerow(row)
