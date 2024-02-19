import csv

# Read from csv:
# data = []
# with open('data.csv', 'r') as f:
#     csv_reader = csv.reader(f)
#     print(type(csv_reader))

#     next(csv_reader)
#     for row in csv_reader:
#         # print(row)
#         data.append(row)

# print(data)

# sorted_data = sorted(data, key=lambda l:l[1])

# # write to csv
# with open('sorted_data.csv', 'w') as fh:
#     csv_writer = csv.writer(fh)
#     csv_writer.writerows(sorted_data)

import csv

# Reading CSV file into iterable of dictionaries
with open('data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)

# # Writing CSV file with dictionaries
# fieldnames = ['Name', 'Age', 'City']
# data = [
#     {'Name': 'John', 'Age': 30, 'City': 'New York'},
#     {'Name': 'Alice', 'Age': 25, 'City': 'San Francisco'}
# ]
# with open('output_dict.csv', 'w', newline='') as file:
#     csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
#     csv_writer.writeheader()
#     csv_writer.writerows(data)
