student = {
    "Python":90,
    "Java":80,
    "SQL":85
}
print(student)
print(student.keys())
print(student.values())
print(student.items())
student["HTML"]=95
print(student)
student["Java"]=88
print(student)
student.pop("SQL")
print(student)
print(student.get("Python"))
print("Total:", sum(student.values()))
print("Average:", sum(student.values())/len(student))
print("Java" in student)
copy_dict = student.copy()
print(copy_dict)