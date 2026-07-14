#Function With Arguments,without return
#Example-1
def print_name():
    print("My Name is Mounika")
print_name()
#Example-2
def college_details():
    print("College : Kalasalingam")
    print("Branch  : CSE AIML")
college_details()
#Example-3
def greeting():
    print("Welcome to Python!")
greeting()
#Example-4
def add():
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print("Sum =", a + b)
add()
#Example-5
def multiply():
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print("Product =", a * b)
multiply()

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