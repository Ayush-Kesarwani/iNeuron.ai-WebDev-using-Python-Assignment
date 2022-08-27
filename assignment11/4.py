n=int(input("Enter any number : "))
sum=0
for i in range(1,(n*2)+1):
    if i%2!=0:
        sum+=i
    else:
        continue
print("Sum = ",sum)