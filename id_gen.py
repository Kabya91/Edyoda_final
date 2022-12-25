import csv

def id_generator():
    with open('Food_Item.csv','r') as inp, open('temp.csv', 'a') as out:
     reader = csv.reader(inp)
     writer = csv.writer(out, delimiter=',')
    #No need to use `insert(), `append()` simply use `+` to concatenate two lists.
     writer.writerow(['ID'] + next(reader))
    #Iterate over enumerate object of reader and pass the starting index as 1.
     writer.writerows([i] + row for i, row in enumerate(reader, 1))
    

id_generator()