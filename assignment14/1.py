# Write a Python script to create a list of first N natural numbers.

naturalNum=[]
n=int(input("Enter any number : "))
for i in range(1,n+1):
    naturalNum.append(i)

print(naturalNum)