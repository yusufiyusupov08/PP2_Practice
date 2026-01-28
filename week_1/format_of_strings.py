price = 59
txt = f"The price is {price} dollars"           # f is to combine 2 types by { }
print(txt)



for x in txt:               #we are printing this string but with the help of "for"
    print(x, end="")        #end is to not printing after every char the space
    
    
for x in txt:               #here will every char be in a new line
    print(x)