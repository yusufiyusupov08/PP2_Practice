word = "abca"
x = ""
count = 0
for n in word:
    
    if n not in x:
        x = x + n
        count = count + 1

print(count)