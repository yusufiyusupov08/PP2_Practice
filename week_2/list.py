# LIST

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


#MY EXAAMPLE

names = ["Yusufi", "Yusupov", "Umedovich"]
print(names)



#ACCESS ITEMS

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print(thislist[-1])


#MY EXAMPLE

names = ["Yusufi", "Yusupov", "Umedovich"]
print(names[2])
print(names[-1])


#Change Item Value

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


#MY EXAMPLE

names = ["Yusufi", "Yusupov", "Umedovich"]
names[0:2] = ["Abdulloh", "Abdulloevich"]
print(names)


#APPEND ITEMS

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


#MY EXAMPLE

names = ["Yusufi", "Yusupov", "Umedovich"]
names.append("Abdulloh")
print(names)


#INSERT ITEMS

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


#MY EXAMPLE 

names = ["Yusufi", "Yusupov", "Umedovich"]
names.insert(1, "Abdulloh")
print(names)   


#EXTEND LIST

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#MY EXAMPLE

names = ["Yusufi", "Yusupov", "Umedovich"]
names2 = ["Abdulloh", "Abdulloevich"]
names.extend(names2)
print(names)


#REMOVE

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


#MY EXAMPLE

names = ["Yusufi", "Yusupov", "Umedovich"]
names.remove("Umedovich")
print(names)


#POP    

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


#MY EXAMPLE

names = ["Yusufi", "Yusupov", "Umedovich"]
names.pop(2)
print(names)


#LOOP THOUGH A LIST 

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
#MY EXAMPLE

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
  
#SORT

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


#MY EXAMPLE

thislist = ["Yusufi", "Yusupov", "Umedovich"]
thislist.sort()
print(thislist)


#COPY

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


#MY EXAMPLE

thislist = ["Yusufi", "Yusupov", "Umedovich"]
mylist = thislist.copy()
print(mylist)


#JOIN

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


#MY EXAMPLE

list1 = ["Yusufi", "Yusupov", "Umedovich"]
list2 = ["Abdulloh", "Abdulloevich"]

list3 = list1 + list2
print(list3)    

