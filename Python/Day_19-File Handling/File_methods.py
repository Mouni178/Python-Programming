file = open("demo.txt","w")
file.write("Python\n")
file.write("Java\n")
file.write("SQL\n")
file.close()
#read()
file = open("demo.txt", "r")
print(file.read())
file.close()
#readline()
file=open("demo.txt","r")
print(file.readline())
print(file.readline())
file.close()
#readlines
file=open("demo.txt","r")
print(file.readlines())
file.close()
#writelines
file=open("languages.txt","w")
languages=[
    "Python\n",
    "Java\n",
    "C++\n",
    "SQL\n"
]
file.writelines(languages)
file.close()
#tell()
file=open("languages.txt","r")
print(file.tell())
print(file.read(6))
print(file.tell())
file.close()
#seek()
file = open("languages.txt","r")
print(file.read(6))
file.seek(0)
print(file.read())
file.close()
#with open()
with open("sample.txt", "w") as file:
    file.write("Python File Handling")
print("File Closed Automatically")