list=[23,11,42,4,8,15]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
print(list)

list=[]
for i in range(6):
    num=int(input("Enter the numbers of list:"))
    list.append(num)
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                temp=list[i]
                list[i]=list[j]
                list[j]=temp
    print(list)