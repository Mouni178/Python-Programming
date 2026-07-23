#Program-1(Store Student Details)
with open("student.txt","w") as file:
    name=input("Enter Name: ")
    age=input("Enter Age: ")
    branch=input("Enter Branch: ")
    file.write("Name : "+ name + "\n")
    file.write("Age : "+ age + "\n")
    file.write("Branch : "+ branch + "\n")
print("Student Details Saved")
#Program-2(Read Student Details)
with open("student.txt","r") as file:
    print(file.read())
#program-3(Count Characters)
with open("student.txt","r") as file:
    data = file.read()
print("Characters =", len(data))
#Program-4(Count Words)
with open("student.txt","r") as file:
    data = file.read()
words = data.split()
print("Words =", len(words))
#Program-5(Count Lines)
with open("student.txt","r") as file:
    lines = file.readlines()
print("Lines =", len(lines))