import csv

with open('iris.data', newline='') as csvfile:
#    print(csvfile)
    reader = csv.DictReader(csvfile)

#    print(reader)
    for row in reader:
        print(row['sepal_width'])

print("\n\n\n\t ***** ne varsa oku *******\n\n\n")
with open("iris.data",'r') as file:
    oku = csv.reader(file)
    for i in oku:
        print(i)