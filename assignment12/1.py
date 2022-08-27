n=int(input("Enter any number : "))

reverse=0
while n!=0:
    d=n%10
    reverse=reverse*10+d
    n//=10
print(reverse)