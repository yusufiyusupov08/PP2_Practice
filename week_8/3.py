name = ["Apple", "Banana", "Water"]
price = [150, 200, 50]

pairs = list(zip(name, price))

print(pairs)

all_pairs = list(filter(lambda x: x[1] > 100, pairs))

print(all_pairs)