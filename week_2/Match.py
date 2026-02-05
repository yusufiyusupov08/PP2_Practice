#The Python Match Statement

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
    
#example 1

status_code = 404

match status_code:
    case 200:
        print("Success!")
    case 400:
        print("Bad Request")
    case 404:
        print("Page Not Found")
    case 500:
        print("Server Error")
    
#Default Value

day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")
    
    
#example 2

command = "RESTART"

match command:
    case "START":
        print("System is starting...")
    case "STOP":
        print("System is shutting down.")
    case _:
        print("Unknown command. Please try again.")
    
    

#Combine Values

day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")
    
    
#example 3

fruit = "Apple"

match fruit:
    case "Apple" | "Banana" | "Cherry":
        print("This is a common fruit.")
    case "Dragonfruit" | "Lychee":
        print("This is an exotic fruit.")
    case _:
        print("Fruit not recognized.")
    
    

#If Statements as Guards

month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
    
    
#example 4

fruit = "Apple"

match fruit:
    case "Apple" | "Banana" | "Cherry":
        print("This is a common fruit.")
    case "Dragonfruit" | "Lychee":
        print("This is an exotic fruit.")
    case _:
        print("Fruit not recognized.")



#example 5


device = "Light"
action = "ON"
battery_level = 15

match device:
    case "Light" | "Fan" | "AC":
        if action == "ON" and battery_level < 20:
            print(f"Warning: Cannot turn on {device}. Battery is too low ({battery_level}%).")
        elif action == "ON":
            print(f"Success: {device} is now active.")
        else:
            print(f"Success: {device} is now off.")

    case "Door":
        print("Security Alert: Door status changed.")

    case _:
        print(f"Error: Device '{device}' not recognized by the system.")