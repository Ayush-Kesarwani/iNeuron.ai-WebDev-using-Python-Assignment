n=int(input("Enter any number : "))

iteration=1
number=n*2
while iteration<=10:
    if number%2==0:
        print(number)
        iteration+=1
    number-=1
        