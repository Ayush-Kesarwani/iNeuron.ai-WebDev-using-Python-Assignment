n=int(input("Enter any number : "))

numList=[]

temp=n
while(temp!=0):
    d=temp%10
    numList.append(d)
    temp//=10
numList.reverse()
print(numList)