import csv
with open("../files//sample2.csv") as csvFile:
    mycsv=csv.DictReader(csvFile)
    list1 = []
    for row in mycsv:
        list1.append(row['Name'])

print(list1)
