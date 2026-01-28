a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""        #you can write how long you want


print(a[:20])           #from start till 20th index
print(a[10:-10:2])    #will print from 10th index till the -10th index from the end but type every other one

#    basic version is  ----->  a[0:len(a):1]