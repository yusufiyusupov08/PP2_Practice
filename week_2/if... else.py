#IF

a = 33
b = 200
if b > a:
  print("b is greater than a")
  
#my example 1

a = 78

if 78%2 == 0:
    print("a is even")
else:
    print("78 is odd")

print("\n")
#my example 2

age = 19

if age >= 18:
    print("You can buy smoke")
    
print("\n")
#my example 3

max_speed = 120
speed = 112
error_speed = 10

if speed+error_speed > max_speed:
    print("You broke the rules")
    print(f"Now pay the fine")
    
    
print("\n")
#The Elif Keyword

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
  
#my example 4
price_ps5 = 1000
games = 100
cash = 450
card = 500

if (card + cash > price_ps5 + games):
    print("You can buy PS5 and Games")
elif (card + cash == 1000):
    print("You can buy PS5, but after you can not afford new games")


#The Else Keyword

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
  
#my example 5


price_ps5 = 1000
games = 100
cash = 450
card = 500

if (card + cash > price_ps5 + games):
    print("You can buy PS5 and Games")
elif (card + cash == 1000):
    print("You can buy PS5, but after you can not afford new games")
else:
    print("You can not buy PS5 and Games")
    
    
#Short Hand If

a = 5
b = 2
if a > b: print("a is greater than b")

#my example 6

age_of_son = 34
age_of_dad = 32

if age_of_dad < age_of_son: print("IT IS NOT POSSIBLE")


#Short Hand If ... Else

a = 2
b = 330
print("A") if a > b else print("B")

#my example


age_of_son = 34
age_of_dad = 32

print("IT IS NOT POSSIBLE") if age_of_dad < age_of_son else print("IT IS POSSIBLE")



