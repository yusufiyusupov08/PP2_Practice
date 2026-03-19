'''demofile.txt

Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!'''

#Example

f = open("demofile.txt")
print(f.read())


f = open("D:\\myfiles\welcome.txt")
print(f.read())

#Using the with statement

with open("demofile.txt") as f:
  print(f.read())
  
#Close Files
  
f = open("demofile.txt")
print(f.readline())
f.close()


# 1
with open("C:\\data\\logs\\app_log.txt", "r") as log_file:
    content = log_file.read()
    print(content)
    
    
# 2
f = open("monthly_report.csv")
header = f.readline()
print("Заголовок документа: " + header)
f.close()


# 3
with open("users_list.txt", "r", encoding="utf-8") as file:
    users = file.readlines()
    for user in users:
        print("Пользователь: " + user.strip()) # .strip() убирает лишние пробелы и переносы
        
        
        
# 4
notes_file = open("todo_list.txt")
print("Мои задачи на сегодня:")
print(notes_file.read())
notes_file.close()


# 5
with open("settings\\config.json", "r", encoding="utf-8") as config:
    data = config.read()
    print("Настройки загружены успешно:")
    print(data)