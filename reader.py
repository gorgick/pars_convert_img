import csv

with open('OMA.csv', 'r') as f:
    csv_data = csv.reader(f)
    for line in csv_data:
        print("".join(line))