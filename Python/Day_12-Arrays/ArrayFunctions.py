#Accessing Elements (Indexing)
marks = [90, 80, 75, 95, 88]
print(marks[0])
print(marks[3])
print(marks[-1])
#Traversing an Array
marks = [90, 80, 75, 95, 88]
for mark in marks:
    print(mark)
#Access Using Index
marks = [90, 80, 75, 95, 88]
for i in range(len(marks)):
    print(marks[i])
#Updating Elements
marks = [90, 80, 75]
marks[1] = 100
print(marks)
#Adding Elements
marks = [90, 80, 75]
marks.append(95)
print(marks)
#Removing Elements
marks = [90, 80, 75]
marks.remove(80)
print(marks)
#Slicing
marks = [90, 80, 75, 95, 88]
print(marks[1:4])
#Reverse
print(marks[::-1])