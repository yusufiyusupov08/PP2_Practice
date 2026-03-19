#Remove the file "demofile.txt":

import os
os.remove("demofile.txt")


#Check if file exists, then delete it:

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
  
  

#Remove the folder "myfolder":

import os
os.rmdir("myfolder")




import os

# 1
file_to_delete = "old_notes.txt"
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print(f"--- Пример 1: Файл '{file_to_delete}' успешно удален ---")
else:
    print(f"--- Пример 1: Файл '{file_to_delete}' не найден, удалять нечего ---")


# 2
path = "C:\\temp\\cache_data.tmp"
try:
    os.remove(path)
    print("--- Пример 2: Временный кэш удален ---")
except FileNotFoundError:
    print("--- Пример 2: Путь не найден ---")


# 3
folder_name = "test_results"
if os.path.exists(folder_name):
    os.rmdir(folder_name)
    print(f"--- Пример 3: Папка '{folder_name}' удалена ---")
else:
    print(f"--- Пример 3: Папка не существует ---")


# 4
files_to_clean = ["temp1.txt", "temp2.txt", "temp3.txt"]
for filename in files_to_clean:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"--- Пример 4: {filename} удален ---")


# 5
new_dir = "temporary_folder"
if not os.path.exists(new_dir):
    os.mkdir(new_dir) # Создаем папку
    print(f"--- Пример 5: Папка '{new_dir}' была создана...")

os.rmdir(new_dir) # И тут же удаляем её
print(f"--- Пример 5: ...и затем успешно удалена ---")