# #Read Mode
# file_r = open("demo.txt","r")
# print(file_r.read())
# file_r.close()

# #Writing Mode
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