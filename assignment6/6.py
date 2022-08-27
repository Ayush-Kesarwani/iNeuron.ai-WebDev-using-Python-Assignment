number = int(input("Enter any number : "))
count=0
while number!=0:
    number=number//10
    count+=1
    
if(count==3):
    print("The number containing 3-digits only")
else:
    print("The number containing ",count,"-digits")