#Example-1
username=input("Enter your Username : ")
password=input("Enter Your Password : ")
verified=input("Enter the verified Status : ")
if username:
    if password:
        if verified:
            print("Login Successful")
        else:
            print("invalid Credentials")
    else:
        print("Password Incorrect")
else:
    print("Username Incorrect")
print()
#Example-2
year=int(input("Enter year:"))
if year%4==0:
    if year%400==0:
        if year%100==0:
            print(year,"is a Leap Year")
        else:
            print(year,"is not a Leap Year")
    else:
        print(year,"is a Leap Year")
else:
    print(year,"is not a Leap Year")
print()
#Example-3
pin = int(input("Enter PIN: "))
balance=10000
if pin==1234:
    amount=int(input("Enter withdrawal amount: "))
    if amount<=balance:
        print("Transaction Successful")
        print("Remaining Balance:", balance - amount)
    else:
        print("Insufficient Balance")
else:
    print("Incorrect PIN")

