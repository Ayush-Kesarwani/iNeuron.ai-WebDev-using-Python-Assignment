naturalNum=[]
n=int(input("Enter any number : "))
count=1
# Write a Python script to create a list of first N odd natural numbers.

num=1
while(count<=n):
    if(num%2!=0):
        count=count+1
        naturalNum.append(num)
        num=num+1
    else:
        num=num+1
print(naturalNum)