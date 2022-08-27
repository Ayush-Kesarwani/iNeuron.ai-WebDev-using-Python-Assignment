num=int(input("Enter any number : "))

found=False

while found!=True:
    num+=1
    for i in range(1,num+1):
        if num%i==0:
            break
    else:
        print(num)
        found=True