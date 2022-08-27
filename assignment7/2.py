print("Type 1 - Addition")
print("Type 2 - Substraction")
print("Type 3 - Multiplication")
print("Type 4 - Division")
n=int(input("Enter your choice from above menu given : "))

n1=eval(input("Enter number 1 : "))
n2=eval(input("Enter number 2 : "))

if n==1:
    print(f"Addition of {n1} and {n2} is {n1+n2}")
elif n==2:
    print(f"Substraction of {n1} and {n2} is {n1-n2}")
elif n==3:
    print(f"Multiplication of {n1} and {n2} is {n1*n2}")
elif n==4:
    print(f"Multiplication of {n1} and {n2} is {n1/n2}")
else:
    print("Invalid choice")