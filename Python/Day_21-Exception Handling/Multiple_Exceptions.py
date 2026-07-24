#Example-1
try:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    print("Result =", num1 / num2)
except ValueError:
    print("Please Enter Numbers Only")
except ZeroDivisionError:
    print("Cannot Divide by Zero")
#Example-2
numbers = [10,20,30,40]
try:
    index = int(input("Enter Index: "))
    print("Element =", numbers[index])
except ValueError:
    print("Please Enter Integer Only")
except IndexError:
    print("Index Out of Range")
#Example-3
student = {
    "name": "Mounika",
    "age": 21
}
try:
    key = input("Enter Key: ")
    print(student[key])
    number = int(input("Enter Any Number: "))
    print("You Entered:", number)
except KeyError:
    print("Key Not Found")
except ValueError:
    print("Please Enter Numbers Only")