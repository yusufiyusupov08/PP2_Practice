
# Example: Open and read the file
f = open("demofile.txt")
print(f.read())

# Example: Open a file on a different location
f = open("D:\\myfiles\\welcome.txt")
print(f.read())


# 1
log_file = open("server_logs.txt")
print(log_file.read())
log_file.close() 


# 2
config = open("C:\\Users\\Admin\\AppData\\settings.ini")
print(config.read())


 # 3
shopping_list = open("grocery_list.txt")
print(shopping_list.read())


# 4
archive = open("/volumes/backup/archive_2025.txt")
print(archive.read())


# 5
notes = open("notes.txt", encoding="utf-8")
print(notes.read())