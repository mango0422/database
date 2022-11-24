import json

with open("temp.json", "r") as f:
    data = json.load(f)
print(data)
print("")
print(data["student"])
print(data["student"][0])
print(data["student"][1])
print(data["student"][2])