import json


def write_inf(data, file_name):
    data = json.dumps(data)
    data = json.loads(str(data))

    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def read_inf(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)


users = read_inf("users.json")
for user in users["users"]:
    if user.get("name") == "Anna":
        print(user.get("flat"))

print(read_inf("users.json"))

data = {"users": []}

data["users"].append({"name": "Anna", "flat": 378})

data["users"].append({"name": "Artem", "flat": 378})

data["users"].append({"name": "Oleh", "flat": 378})

data["users"].append({"name": "Lilya", "flat": 379})

data["users"].append({"name": "Oleksii", "flat": 377})

data["users"].append({"name": "Yurii", "flat": 380})

data["users"].append({"name": "Olena", "flat": 380})

data["users"].append({"name": "Dmitro", "flat": 381})


write_inf(data, "users.json")
