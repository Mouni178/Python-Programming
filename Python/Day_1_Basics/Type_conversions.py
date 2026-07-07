"""price = "99.99"
print(type(price))
price = float(price)
print(type(price))"""
"""
num = "100"
print(type(num))
num = int(num)
print(type(num))"""
# Original Variables
name = "Mounika"
age = "21"
cgpa = "9.01"
marks = 95
salary = 50000.75
print("--ORIGINAL VALUES--")
print(name, type(name))
print(age, type(age))
print(cgpa, type(cgpa))
print(marks, type(marks))
print(salary, type(salary))
# String to Integer
age = int(age)
# String to Float
cgpa = float(cgpa)
# Integer to Float
marks_float = float(marks)
# Float to Integer
salary_int = int(salary)
# Integer to String
marks_string = str(marks)
# Integer to Boolean
marks_bool = bool(marks)
# String to Boolean
name_bool = bool(name)
print("\n--AFTER TYPE CONVERSION--")
print(age, type(age))
print(cgpa, type(cgpa))
print(marks_float, type(marks_float))
print(salary_int, type(salary_int))
print(marks_string, type(marks_string))
print(marks_bool, type(marks_bool))
print(name_bool, type(name_bool))
