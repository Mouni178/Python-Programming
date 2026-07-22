#Creating Files
file=open("sample.txt","w")
print("file created Successfully")
file.close()
#write
file=open("student.txt","w")
file.write("name:Mounika\n")
file.write("Branch:CSE-AIML\n")
file.write("CGPA:9.01\n")
file.close()
print("Data Written Successfully")
#read
file=open("student.txt","r")
content=file.read()
print(content)
file.close()
#Append
file=open("student.txt","a")
file.write("College:Kare\n")
file.close()
print("data Appended Successfully")
#read Again
file=open("student.txt","r")
print(file.read())
file.close()