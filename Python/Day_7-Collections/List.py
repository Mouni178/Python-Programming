#Creating A List
fruits=["Apple","Orange","Banana","Guava","Watermelon","Kiwi"]
print(fruits)

#Accessing Elements
print(fruits[0])
print(fruits[2])
print(fruits[5])
print(fruits[-1])

#Slicing
print(fruits[1:3])
print(fruits[1:5:2])
print(fruits[1:])
print(fruits[:5])
print(fruits[::-1])

#Updating List
fruits[1] ="Grapes"
print(fruits)

#List Length
print(len(fruits))

#Check Membership
print("Apple" in fruits)
print("Pineapple" not in fruits)

#Iterate List
for fruit in fruits:
    print(fruit)