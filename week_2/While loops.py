#while

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
  
#example 1

fruits = ["Apple", "Banana", "Cherry", "Date"]
index = 0

while index < len(fruits):
    print(f"Current fruit: {fruits[index]}")
    index += 1
    
#example 2

fuel_liters = 5

while fuel_liters > 0:
    print(f"Car is driving... Fuel left: {fuel_liters}L")
    fuel_liters -= 1

print("Out of gas!")

#example 3

phone_model = ""

while phone_model.lower() != "iphone":
    phone_model = input("Enter a phone brand (type 'iPhone' to stop): ")
    print(f"Checking {phone_model}...")

print("Found the iPhone!")

#example 4

burgers_in_stock = 10
ordered = 0

while burgers_in_stock > 5:
    ordered += 1
    burgers_in_stock -= 1
    print(f"Order #{ordered} served. Burgers remaining: {burgers_in_stock}")

print("Inventory low! Please restock.")


#example 5

distance_to_mars = 0
target_distance = 100

while distance_to_mars < target_distance:
    distance_to_mars += 25
    print(f"Spaceship has traveled {distance_to_mars} million miles.")

print("Arrival at Mars!")