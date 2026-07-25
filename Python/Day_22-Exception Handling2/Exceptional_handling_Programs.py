#Example-1(Safe Calculator)
try:
    a=int(input("Enter First Number: "))
    b=int(input("Enter Second Number: "))
    print("Division =",a/b)
except ZeroDivisionError:
    print("Cannot Divide by Zero")
except ValueError:
    print("Please Enter Valid Numbers")
#Example-2(Safe List Access)
numbers=[100, 200, 300]
try:
    index=int(input("Enter Index: "))
    print(numbers[index])
except IndexError:
    print("Index Out of Range")
except ValueError:
    print("Invalid Input")
#Example-3(Dictionary Access)
student={
    "name":"Mounika",
    "branch":"CSE AIML"
}
try:
    key=input("Enter Key: ")
    print(student[key])
except KeyError:
    print("Key Not Found")
#Example-4(
try:
    file = open("student.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File Does Not Exist")
#Example5(Logic Example)
password = "python123"
try:
    user = input("Enter Password: ")
    if user != password:
        raise Exception("Wrong Password")
    print("Login Successful")
except Exception as e:
    print(e)