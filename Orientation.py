import csv

with open("RatingsInput.csv", 'r') as infile:
    reader = csv.reader(infile, delimiter=",")
    header = next(reader)
    print(header)