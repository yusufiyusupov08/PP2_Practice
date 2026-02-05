#SET

thisset = {"apple", "banana", "cherry"}
print(thisset)


#MY EXAMPLE

names = {"Yusufi", "Yusupov", "Umedovich"}
print(names)


#ACCESS ITEMS

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
#MY EXAMPLE

names = {"Yusufi", "Yusupov", "Umedovich"}

for x in names:
  print(x)
  
  
#ADD ITEMS

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


#MY EXAMPLE

names = {"Yusufi", "Yusupov", "Umedovich"}

names.add("Abdulloh")

print(names)


#REMOVE ITEM

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


#MY EXAMPLE

names = {"Yusufi", "Yusupov", "Umedovich"}

names.remove("Umedovich")

print(names)


#LOOP SET

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
#MY EXAMPLE

names = {"Yusufi", "Yusupov", "Umedovich"}

for x in names:
  print(x)
  

#JOIN SET

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


#MY EXAMPLE

name1 = {"Yusufi", "Yusupov", "Umedovich"}
name2 = {"Abdulloh", "Abdulloevich"}

name3 = name1.union(name2)
print(name3)


#FROZENSET

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))


#MY EXAMPLE

x = frozenset({"Yusufi", "Yusupov", "Umedovich"})
print(x)
print(type(x))


