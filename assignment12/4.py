import math

min = int(input("Enter min number : "))
max = int(input("Enter max number : "))

for i in range(min,max+1):
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            break
    else:
        print(i)