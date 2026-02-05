'''Boolean Values'''

#the result will be true or false
print(10 > 9)
print(10 == 9)
print(10 < 9)


#examples
print(20266 > 2029)
print(0 == 0)
print(34 < 35)
print(2007 == 2008)
print(1 < 10)


#TRUE
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


#FALSE
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})



#examples

#true
print(bool("Yusufi"))
print(bool(18))
print(bool(("BMW", "AUDI", "Mercedes")))
print(bool(["BMW", "AUDI", "Mercedes"]))
print(bool({"name" : "Yusufi", "age" : 17}))



#false
print(bool(""))
print(bool(0))
print(bool())
print(bool([]))
print(bool(None))
print(bool(False))