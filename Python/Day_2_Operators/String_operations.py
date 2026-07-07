name="Mounika"
name2="Royal"
age=21
#Indexing
print(name[0])
print(name[-1])
print(name[6])
#Slicing
print(name[:3])
print(name[2:])
print(name[::3])
print(name[-1::2])
print(name[::-1])
#Concatenation
print(name + " " + name2)
#Repetition
print(name2*4)
#Length,Upper,Lower,titlecase,capatilasize
print(len(name))
print(name.upper())
print(name2.lower())
print(name2.title())
print(name2.capitalize())
#Replace
print(name.replace("a","i"))
#Find
print(name.find("s"))
#count
print(name.count("a"))
#Split
skills = "Python Java SQL"
print(skills.split())
#join
languages = ["Python", "Java", "SQL"]
print(", ".join(languages))
#strip-remove spaces,lstrip remove left strip,rstrip remove the right strip
text = "   Python   "
print(text.strip())
print(text.lstrip())
print(text.rstrip())
#swap case
print(name.swapcase())
#isalpha,isnum,isalnum,islower,isupper
print("Python123".isalpha())
print("12345".isdigit())
print("123abc".isdigit())
print("Python123".isalnum())
print("Python 123".isalnum())
print("python".islower())
print("Python".islower())
print("python".isupper())
print("Python".isupper())
#Escape Characters
print("Hello\nWorld")
print("Hello\tWorld")
print("Python \"Programming\"")
#String Formatting
print(f"My name is {name}")
print(f"My age is {age}")
