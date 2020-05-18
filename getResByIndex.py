import json
from collections import OrderedDict

path_to_file = "data.json"

with open(path_to_file) as data_file:
    data = OrderedDict(json.load(data_file))
    # data = json.load(data_file)

length = len(data["data"])

print(length)
print(type(data))
item = list(data.items())
print(item[0].values())

# for i in range(length):
#     print(data["data"].values()[i]["name"])