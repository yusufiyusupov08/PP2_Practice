import json
import re


data = json.loads(input())

for item in data:
    status_value = item["status"]
    
    
    
    if re.fullmatch(r"Error\d{3}", status_value):
        print(item["id"])
    

a = re.findall(r"Error\d{3}", status_value)
print(a)