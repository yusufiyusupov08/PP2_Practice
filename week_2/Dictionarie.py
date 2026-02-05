# Dictionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


#MY EXAMPLE

names = {
  "first": "Yusufi",
  "second": "Yusupov",
  "third": "Umedovich"
}
print(names)


#ACCESS ITEMS

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)


#MY EXAMPLE

names = {
  "first": "Yusufi",
  "second": "Yusupov",
  "third": "Umedovich"
}
x = names["second"]
print(x)


#CHANGE VALUES

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)


#MY EXAMLPE

names = {
  "first": "Yusufi",
  "second": "Yusupov",
  "third": "Umedovich"
}
names["first"] = "Abdulloh"
print(names)


#ADD

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


#MY EXAMPLE

names = {
  "first": "Yusufi",
  "second": "Yusupov",
  "third": "Umedovich"
}
names["fourth"] = "Abdulloevich"
print(names)


#REMOVE

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


#MY EXAMPLE

names = {
  "first": "Yusufi",
  "second": "Yusupov",
  "third": "Umedovich"
}
names.pop("third")
print(names)


#LOOP

for x, y in thisdict.items():
  print(x, y)


#MY EXAMPLE

for x, y in names.items():
  print(x, y)


#COPY

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


#MY EXAMPLE

names = {
  "first": "Yusufi",
  "second": "Yusupov",
  "third": "Umedovich"
}
mydict = names.copy()
print(mydict)


#NESTED DICTIONARIES

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)


#MY EXAMPLE

myfamily2 = {
  "child1" : {
    "name" : "ARTUR",
    "year" : 1999
  },
  "child2" : {
    "name" : "FLORA",
    "year" : 2005
  },
  "child3" : {
    "name" : "FAUNA",
    "year" : 2012
  }
}

print(myfamily2)