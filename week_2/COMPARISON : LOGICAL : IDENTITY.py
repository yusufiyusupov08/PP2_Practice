#   COMPARISON

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#MY EXAMPLE

print(5 == 5)
print(10 != 10)
print(7 > 3)
print(8<10)
print(9>=9)
print(10<=9)

#   LOGICAL

x = 5

print(x > 0 and x < 10)
print(x < 5 or x > 10)
print(not(x > 3 and x < 10))


#MY EXAMPLE

x = 5

print(x > 3 and x < 15)
print(x > 3 or x < 4)
print(not(x > -1234576890 and x < 1234567890))
print(x != 0 and x > 0)
print(x != 0 or x > 0)
print(not(x != 0 and x > 0))


#   IDENTITY

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

#MY EXAMPLE

x = ["Yusufi", "Yusupov"]
y = ["Yusufi", "Yusupov"]
z = x

print(x is z)
print(x is y)
print(x == y)


#   MEMBERSHIP

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
print("pineapple" not in fruits)

#MY EXAMPLE

x = ["Yusufi", "Yusupov", "Umedovich"]

print("Yusufi" in x)
print("Umedovich" not in x)