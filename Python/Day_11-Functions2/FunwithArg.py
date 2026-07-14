#Function With Arguments,without return
#Example-1
def print_name(name):
    print("My Name is", name)
print_name("Mounika")
#Example-2
def greeting(name):
    print("Welcome", name)
greeting("Mounika")
#Example-3
def add(a, b):
    print("Sum =", a + b)
add(10, 20)
#Example-4
def subtract(a, b):
    print("Difference =", a - b)
subtract(50, 20)
#Example-5
def multiply(a, b):
    print("Product =", a * b)
multiply(8, 5)
##Function with arguments and with return
#Example-1
def add(a, b):
    return a + b
result = add(10,20)
print(result)
#Example-2
def multiply(a, b):
    return a * b
print(multiply(5,6))
#Eample-3
def square(number):
    return number * number
print(square(9))
#Example-4
def area_circle(radius):
    area = 3.14 * radius * radius
    return area
print(area_circle(5))
#Example-5
def bmi(weight, height):
    return weight / (height ** 2)
print(bmi(60,1.65))