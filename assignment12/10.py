num1=int(input("Enter number 1 : "))
num2=int(input("Enter number 2 : "))

hcf=0

min=num1 if num1<num2 else num2

for i in range(2,min+1):
    if num1%i==0 and num2%i==0:
        hcf=i
print(hcf)