string=input("Enter a String : ")
print(string)
#Reverse a String
print("Reverse =", string[::-1])
#Palindrome
string = input("Enter a string: ")
if string==string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
#Count Vowels
string=input("Enter a String:")
count=0
for ch in string.lower():
    if ch in "aeiou":
        count += 1
print("Vowels=",count)
#Count Consonants
string=input("\nEnter a string: ")
count=0
for ch in string.lower():
    if ch.isalpha() and ch not in "aeiou":
        count+=1
print("Consonants =",count)
#Count Digits
string = input("\nEnter a string: ")
count = 0
for ch in string:
    if ch.isdigit():
        count += 1
print("Digits =", count)
#Count Uppercase
string = input("\nEnter a string: ")
count = 0
for ch in string:
    if ch.isupper():
        count += 1
print("Uppercase =", count)
#count LowerSpaces
string = input("\nEnter a string: ")
count = 0
for ch in string:
    if ch.islower():
        count += 1
print("Lowercase =", count)
#Count Spaces
string=input("\nEnter a string: ")
count=0
for ch in string:
    if ch == " ":
        count += 1
print("Spaces =", count)
#Remove Spaces
string = input("\nEnter a string: ")
print(string.replace(" ", ""))
#Count Words
string=input("\nEnter a sentence: ")
words=string.split()
print("Words=", len(words))