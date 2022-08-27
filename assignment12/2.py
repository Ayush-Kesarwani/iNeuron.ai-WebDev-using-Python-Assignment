import math
n=int(input("Enter any number : "))

for i in range(2,int(math.sqrt(n))):
    if n%i==0:
        print("Not Prime")
        break
else:
    print("Prime")


