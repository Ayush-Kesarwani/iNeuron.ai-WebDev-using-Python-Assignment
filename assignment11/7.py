n=int(input("Enter any number : "))
count=0
while n!=0:
    count+=1
    n//=10
print("Number of digits are ",count)