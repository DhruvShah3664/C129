import csv
dataset_1 = []
dataset_2 = []


with open("final.csv", "r")as f:
    csvr = csv.reader(f)

    for row in csvr:
        dataset_1.append(row)


with open("archive_dataset_sorted1.csv", "r")as f:
    csvr = csv.reader(f)

    for row in csvr:
        dataset_2.append(row)

headers1 = dataset_1[0]
planet_data1 = dataset_1[1:]

headers2 = dataset_2[0]
planet_data2 = dataset_2[1:]

headers = headers1+ headers2
planet_data = []

for index, data_row in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])

with open("merged_dataset.csv", "a+")as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)