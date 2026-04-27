import re
import json

text = {"Apple Price is": 150, "Banana price is": 200, "Water is": 50, "Country is": "True"}
        
j_text = json.dumps(text)

word = re.findall(r'[A-Z][a-z]+', j_text)

print(word)

jl = json.loads(j_text)

print(jl)
print(j_text)


with open("test.txt", "w") as f:
    f.write(j_text)
    
    
with open("test.txt", "a") as f:
    f.write("\nHello, Python!")