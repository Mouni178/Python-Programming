#Program-1
with open("student.txt","w") as file:
    name=input("Enter Name: ")
    age=input("Enter Age: ")
    branch=input("Enter Branch: ")
    file.write("Name : "+ name + "\n")
    file.write("Age : "+ age + "\n")
    file.write("Branch : "+ branch + "\n")
print("Student Details Saved")
#Program-2
with open("student.txt","r") as file:
    print(file.read())
#program-3
with open("student.txt","r") as file:
    data = file.read()
print("Characters =", len(data))