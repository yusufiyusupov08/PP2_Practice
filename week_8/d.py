import json
import re

t = json.loads(input())

print(t)

pattern = r"^@[a-z_]*_[a-z_]*$"

for item in t:
    id = item["user_id"]
    name = item["handle"]
    
    if re.fullmatch(pattern, name):
        print(id)