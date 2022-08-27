num1=int(input("Enter number 1 : "))
num2=int(input("Enter number 2 : "))

max=num1 if num1>num2 else num2

# while(True):
#     if max%num1==0 and max%num2==0:
#         print(max)
#         break
#     max=max+1

lcm=1
for i in range(2,max+1):
    if num1%i==0 and num2%i!=0:
        num1//=num1
        lcm=lcm*i
    elif num1%i!=0 and num2%i==0:
        num2//=num2
        lcm=lcm*i
    elif num1%i==0 and num2%i==0:
        num1//=num1
        num2//=num2
        lcm=lcm*i
    else:
        continue
print(lcm)
    

