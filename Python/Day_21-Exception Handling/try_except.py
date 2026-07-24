#Example-1
try:
    numbers=[10,20,30,40,50]
    index=int(input("Enter Index:"))
    print(numbers[index])
except IndexError:
    print("Invalid Index")

#Example-2
try:
    number = int(input("Enter Number: "))
    print(100 / number)
except ZeroDivisionError:
    print("Cannot Divide by Zero")
except ValueError:
    print("Enter Numbers Only")
#Example-3
try:
    age=int(input("Enter Your Age:"))
    print("your Age is :",age)
except ValueError:
    print("Please Enter Numbers Only")
#Example-4
numberr=[10,20,30,40,50]
try:
    num=int(input("Enter Number to Search:"))
    position=numberr.index(num)
    print("Found at index",position)
except ValueError:
    print("Number Not Found in the List")
