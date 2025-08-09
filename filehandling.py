#Read Mode
# file_r = open("demo.txt","r")
# print(file_r.read())
# file_r.close()

#Writing Mode
# file_w = open("demo.txt","w")
# file_w.write("I Am 12 Years Old.")
# file_w.close()

#Append Mode
# file_a = open("demo.txt","a")
# file_a.write(f" I Love Coding!")
# file_a.close()


file_line = open("demo.txt","r")
counter = 0
lines = file_line.read()
line_list = lines.split(".")
for i in line_list:
    if i:
        counter += 1
        print(i)

print(f"This Are The Number Of Lines In This Python File:{counter}")
#Operations#01: Reading Characters From A File
file1 = open("new_file.txt","r")
print(f"Reading 4 Characters Only: {file1.read(4)}")
#The Arguements Inside The Main Function Denotes The Characters Inside The File
file1.close()

#Operations#02: Reading Only 1 Lines From A File
file2 = open("new_file.txt","r")
print(file2.readline())
file2.close()

#Operations#3: Reading All Lines Using Loop From A txt File
file3 = open("new_file.txt","r")
for x in file3:
    print(x)
file3.close()

#Operations#04: Reading All Lines Without Loop
file4 = open("new_file.txt","r")
print(file4.readlines())
file4.close()

#Operations#05: Filtering Files And Extracting Them In Another File
#Removing Lines From A File
file5 = open("new_file.txt","r")
file6 = open("updated_file.txt","w")

for line in file5.readlines():
    if not line.startswith("Bangladesh"):
        print(line)
        file6.write(line)
file5.close()
file6.close()

#Operations#06: Reading Odd Lines From A File
file7 = open("new_file.txt","r")
file8 = open("fresh_file.txt","w")
contents = file7.readlines()
print(type(contents))
for i in range(1,len(contents)+1):
    if (i%2 != 0):
        file8.write(contents[i-1])
    else:
        pass
file7.close()
file8.close()