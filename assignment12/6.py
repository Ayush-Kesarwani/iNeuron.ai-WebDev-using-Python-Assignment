import math
n = int(input("Enter any number : "))

count=1
num=2
while(count<=n):
    for i in range(2, int(math.sqrt(num))+1):
        if(num%i==0):
            break
    else:
        print(num)
        count+=1
    num+=1
    