#Example-1
def print_name():
    print("My name is Mounika")
print_name()
print()
#Example-2
def college_details():
    print("College : Kalasalingam Academy of Research and Education")
    print("Branch  : CSE (AI & ML)")
    print("CGPA    : 9.01")
college_details()
print()
#Example-3
def add_numbers():
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print("Sum =", a + b)
add_numbers()
#Example-4
def multiply_numbers():
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print("Multiplication =", a * b)
multiply_numbers()
#Example-5
def greeting():
    print("Welcome to Python Programming!")
    print("Have a Nice Day!")
greeting()
#Example-6
def calculate_bmi():
    weight = float(input("Enter Weight (kg): "))
    height = float(input("Enter Height (m): "))
    bmi = weight / (height ** 2)
    print("BMI =", round(bmi, 2))
calculate_bmi()
#Example-7
def simple_interest():
    principal = float(input("Enter Principal Amount: "))
    rate = float(input("Enter Rate of Interest: "))
    time = float(input("Enter Time (Years): "))
    si = (principal * rate * time) / 100
    print("Simple Interest =", si)
simple_interest()
#Example-8
def area_of_circle():
    radius = float(input("Enter Radius: "))
    area = 3.14 * radius * radius
    print("Area of Circle =", area)
area_of_circle()
#Example-9
def electricity_bill():
    units = int(input("Enter Units Consumed: "))
    bill = units * 7.5
    print("Electricity Bill = ₹", bill)
electricity_bill()
#Example-10
def student_details():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    college = input("Enter College: ")
    branch = input("Enter Branch: ")
    cgpa = float(input("Enter CGPA: "))
    print("\n-------- Student Details --------")
    print("Name    :", name)
    print("Age     :", age)
    print("College :", college)
    print("Branch  :", branch)
    print("CGPA    :", cgpa)

