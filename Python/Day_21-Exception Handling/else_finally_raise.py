#else,finally
try:
    a=10
    b=2
    print(a/b)
except ZeroDivisionError:
    print("Division Error")
else:
    print("No Exception Occurred")
finally:
    print("Program Finished")
#raise
age = int(input("Enter Age: "))
if age<18:
    raise Exception("Age must be 18 or above")
print("Eligible")