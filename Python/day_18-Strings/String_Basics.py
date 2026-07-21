#Creating Strings
name="Mounika"
print(name)
#Single Quotes
name2='Mouni'
print(name2)
#Double Quotes
name3="Jayanth"
print(name3)
#Triple Quotes
name4=""" Hello
Welcome
Python"""
print(name4)
#Indexing
string="Python"
print(string[0])
print(string[5])
print(string[-1])
#Slicing
print(string[1:4])
print(string[:3])
print(string[2:])
print(string[::-1])
#Concatenation
first="Hello"
second="Python"
print(first + " " + second)
#Repetition
print("Mouni"*4)
#Membership
print("p" in string)
print("c" in string)
print("z" not in string)
print("t" not in string) 
#Length
print(len(string))
print(len(name))
print(len(name4))
#Traversing
for ch in name:
    print(ch)