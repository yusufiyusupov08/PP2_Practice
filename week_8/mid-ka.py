import json

student = '{"city": "Almaty", "temp": 15, "is_sunny": true}'



dict = json.loads(student)

print(dict)
print(type(dict), "\n")

dict["temp"] += 5

dict["country"] = "Kazakhstan"

updated_json = json.dumps(dict)

print(dict, "\n")
print(updated_json)
print(type(updated_json))