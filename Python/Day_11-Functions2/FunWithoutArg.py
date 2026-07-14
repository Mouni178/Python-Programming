##Functions without arguments without return
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
##Functions without Arguments with return
#Example-1
def add():
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    return a + b
print("Sum =", add())
#Example-2
def square():
    number = int(input("Enter Number: "))
    return number * number
print("Square =", square())
#Example-3
def cube():
    number = int(input("Enter Number: "))
    return number ** 3
print("Cube =", cube())
#Example-4
def area_circle():
    radius = float(input("Enter Radius: "))
    return 3.14 * radius * radius
print("Area =", area_circle())
#Example-5
def bmi():
    weight = float(input("Enter Weight: "))
    height = float(input("Enter Height: "))
    return weight / (height ** 2)
print("BMI =", round(bmi(), 2))