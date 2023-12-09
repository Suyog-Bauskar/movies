import csv
file = open("movies.csv", 'r')
csvFile = csv.reader(file)
for lines in csvFile:
    print("Rating: ", lines[4])
