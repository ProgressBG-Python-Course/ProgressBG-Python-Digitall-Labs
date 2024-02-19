import json

# json_str = """
#     [
#         {
#                 "name": "apple",
#                 "price": 1.80
#         },
#         {
#                 "name": "orange",
#                 "price": 2.10
#         },
#         {
#                 "name": "bananas",
#                 "price": 1.60
#         }
#     ]
# """

# fruits = json.loads(json_str)


# with open('./data.json') as fh:
#     fruits = json.load(fh)

# for fruit in fruits:
#     print(fruit)

# d = {
#     'is_adult':True,
#     'data':[1,2,3,]
# }

# d_json = json.dumps(d)
# print(d_json)


### Read JSON => SORT data => Write JSON
# Read JSON
with open('./data.json') as fh:
    data = json.load(fh)


# SORT data
sorted_data = sorted(data, key=lambda d:d['price'])
print(sorted_data)

# Write JSON
with open('./sorted_data', 'w') as fh:
    json.dump(sorted_data, fh, indent=4)

