student={
    "Name":"Mounika",
    "Age":21,
    "Branch":"CSE",
    "CGPA":9.01
}
print(student)
#Access Values
print(student["Name"])
print(student["CGPA"])
#Using get()
print(student.get("Branch"))
#Update Value
student["CGPA"]=9.05
print(student)
#Add New Key
student["City"] = "Hyderabad"
print(student)
#Delete Key
del student["Age"]
print(student)
#Membership
print("Name" in student)
# Loop
for key in student:
    print(key,":",student[key])