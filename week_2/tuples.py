#TUPLE 

thistuple = ("apple", "banana", "cherry")
print(thistuple)


#MY EXAMPLE

names = ("Yusufi", "Yusupov", "Umedovich")
print(names)


#ACCESS ITEMS

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


#MY EXAMPLE

names = ("Yusufi", "Yusupov", "Umedovich")
print(names[2])


#UPDATE TUPLES

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


#MY EXAMPLE 

x = ("Yusufi", "Yusupov", "Umedovich")
y = list(x)
y[2] = "Abdulloh"
x = tuple(y)

print(x)


#UNPACK TUPLES

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


#MY EXAMPLE

names = ("Yusufi", "Yusupov", "Umedovich")

(first, second, third) = names

print(first)
print(second)
print(third)


#LOOP TUPLES

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  
#MY EXAMPLE

thistuple = ("Yusufi", "Yusupov", "Umedovich")
for x in thistuple:
  print(x)
  
  
#JOIN TUPLES

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


#MY EXAMPLE

tuple1 = ("Yusufi", "Yusupov", "Umedovich")
tuple2 = ("Abdulloh", "Abdulloevich")

tuple3 = tuple1 + tuple2
print(tuple3)


