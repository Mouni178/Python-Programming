student = {
    "Math":90,
    "Science":95,
    "English":88
}
#Total Marks
print(sum(student.values()))
#Average
print(sum(student.values())/len(student))
#Highest Marks
print(max(student.values()))
#Lowest Marks
print(min(student.values()))
#Print All Subjects
for subject,marks in student.items():
    print(subject,"=",marks)