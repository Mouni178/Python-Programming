numbers=[17,8,23,67,28,14,28,59,3,76]
#append
numbers.append(40)
print(numbers)

#extend()
numbers.extend([50, 60])
print(numbers)

# insert()
numbers.insert(1, 15)
print(numbers)

# remove()
numbers.remove(23)
print(numbers)

# pop()
numbers.pop()
print(numbers)
numbers.pop(1)
print(numbers)

# clear()
temp = [1, 2, 3]
temp.clear()
print(temp)

# index()
print(numbers.index(67))

# count()
numbers.append(30)
print(numbers.count(30))

# sort()
marks = [55, 12, 98, 40]
marks.sort()
print(marks)

# reverse()
marks.reverse()
print(marks)

# copy()
new_marks = marks.copy()
print(new_marks)
