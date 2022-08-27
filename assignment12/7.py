# The HCF of two co-prime numbers is always 1. As 1 is the only common factor of two co-prime numbers.

num1=int(input("Enter 1st number : "))
num2=int(input("Enter 2nd number : "))

hcf=0

min=num1 if num1<num2 else num2

for i in range(1,min+1):
    if num1%i==0 and num2%i==0:
        hcf=i

if(hcf==1):
    print(f"{num1} and {num2} are co-prime numbers")
else:
    print(f"{num1} and {num2} are not co-prime numbers")