import csv
with open("iris.names",'r') as f :
    dosyaoku = csv.reader(f)
    for i in dosyaoku:
        print(i)