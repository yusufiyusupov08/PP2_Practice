#Open the file "demofile.txt" and append content to the file:
with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())
  
  
  
#Open the file "demofile.txt" and overwrite the content:
  
with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())
  
  
  
#Create a new file called "myfile.txt":

f = open("myfile.txt", "x")






# 1
with open("daily_log.txt", "a", encoding="utf-8") as log:
    log.write("\nНовая запись от 19 марта: Все системы работают стабильно.")

print("--- Пример 1 (Дозапись) выполнен ---")


# 2
with open("settings.conf", "w", encoding="utf-8") as config:
    config.write("theme=dark\nlanguage=ru\nnotifications=on")

print("--- Пример 2 (Перезапись) выполнен ---")


# 3
try:
    f = open("unique_report_id_99.txt", "x")
    f.write("Этот файл был создан с нуля.")
    f.close()
    print("--- Пример 3 (Создание) выполнен ---")
except FileExistsError:
    print("--- Пример 3: Файл уже существует! ---")


# 4
with open("temp_buffer.txt", "w") as temp:
    temp.write("") 

print("--- Пример 4 (Очистка) выполнен ---")


# 5
filename = "message.txt"

with open(filename, "w", encoding="utf-8") as f:
    f.write("Привет! Это финальный пример кода.")

with open(filename, "r", encoding="utf-8") as f:
    result = f.read()
    print("Содержимое файла из Примера 5:")
    print(result)