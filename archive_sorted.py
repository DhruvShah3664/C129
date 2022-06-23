import csv
data =[]
with open("archive_dataset.csv", "r")as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data.append(row)

headers = data[0]
planet_data = data[1:]

#converting all the planet names to lower case
for data_point in planet_data:
    data_point[2] = data_point[2].lower()

#sorting planet name in alphabetical order
planet_data.sort(key = lambda planet_data: [2])
with open("archive_dataset_sorted.csv", "a+")as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)

#remove blank lines
with open("archive_dataset_sorted.csv")as input, open("archive_dataset_sorted1.csv", "w", newline  = "")as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)