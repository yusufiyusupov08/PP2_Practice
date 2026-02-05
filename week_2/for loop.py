#FOR LOOP

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
  
#MY EXAMPLE 1
fruits = ["Apple", "Banana", "Cherry", "Date"]

for fruit in fruits:
    print(f"Current fruit: {fruit}")
    
    
#MY EXAMPLE 2
for fuel_liters in range(5, 0, -1):
    print(f"Car is driving... Fuel left: {fuel_liters}L")

print("Out of gas!")


#MY EXAMPLE 3
phones = ["Samsung", "Pixel", "iPhone", "Nokia"]

for phone in phones:
    print(f"Checking {phone}...")
    if phone.lower() == "iphone":
        print("Found the iPhone!")
        break
    
    
#MY EXAMPLE 4
burgers_in_stock = 10

for order_num in range(1, 6):
    burgers_in_stock -= 1
    print(f"Order #{order_num} served. Burgers remaining: {burgers_in_stock}")

print("Inventory low! Please restock.")


#MY EXAMPLE 5
target_distance = 100

for distance in range(25, target_distance + 1, 25):
    print(f"Spaceship has traveled {distance} million miles.")

print("Arrival at Mars!")

