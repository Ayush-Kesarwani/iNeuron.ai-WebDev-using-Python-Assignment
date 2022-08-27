n1=int(input("Enter 1st number : "))
n2=int(input("Enter 2nd number : "))
n3=int(input("Enter 3rd number : "))

if n1==n2==n3:
    print(n1)
elif n1>=n2 and n1>=n3:
    print(n1, " is the greater among the three")
elif n2>=n1 and n2>=n3:
    print(n2," is the greater among the three")
else:
    print(n3, " is the greater among the three")
    