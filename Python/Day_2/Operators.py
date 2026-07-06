#Arithmetic Operators
num1=int(input("Enter your First Number:"))
num2=int(input("Enter your Second Number:"))
print("Addition of two numbers:",num1+num2)
print("Subtraction of two numbers:",num1-num2)
print("Multiplication of two numbers:",num1*num2)
print("Division of two numbers:",num1/num2)
print("Floor Division of two numbers:",num1//num2)
print("Modulus of two numbers:",num1%num2)
print("Power of two numbers:",num1**num2)
print()
#Assignment Operators
x = 10
print("Original Value :", x)
x += 5
print("After += 5 :", x)
x -= 3
print("After -= 3 :", x)
x *= 2
print("After *= 2 :", x)
x /= 4
print("After /= 4 :", x)
x //= 2
print("After //= 2 :", x)
x %= 2
print("After %= 2 :", x)
x **= 3
print("After **= 3 :", x)
print()
#Comparision Operators
print("num1!=num2 :", num1!=num2)      
print("num1>num2  :", num1>num2)       
print("num1<num2  :", num1<num2)   
print("num1>=num2 :", num1>=num2)     
print("num1<=num2 :", num1<=num2)      
print()
#Logical Operators
age = 21
cgpa = 9.01
print("age > 18 and cgpa > 8 :", age > 18 and cgpa > 8)
print("age > 25 or cgpa > 8 :", age > 25 or cgpa > 8)
print("not(age > 18) :", not(age > 18))
print()
#Bitwise Operators
print("num1 | num2 =",num1|num2)
print("num1 ^ num2 =",num1^num2)
print("!num1 =",~num1)
print("num1 << 1 =",num1<<1)
print("num1 >> 1 =",num1>>1)
#Membership operators
name="Mounika Royal"
print("ou" in name)
print("p" in name)
