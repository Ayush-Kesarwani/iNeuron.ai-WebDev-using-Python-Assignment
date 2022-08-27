n=int(input("Enter any number : "))
sum=0
while n!=0:
    d=n%10
    sum+=d
    n//=10
print("Sum of digits are ",sum)