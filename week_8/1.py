import json

def evens_gen(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
            
my_list = list(evens_gen(10))

print((my_list))

json_list = json.dumps(my_list)

