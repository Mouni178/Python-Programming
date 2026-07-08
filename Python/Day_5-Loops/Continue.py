#Example-1
for i in range(10):
    if i == 5:
        continue
    print(i)
print()
#Example-2
name="Mounika"
i=0
while i < len(name):
    if name[i]=="k":
        i+=1
        continue
    print(name[i])
    i += 1
