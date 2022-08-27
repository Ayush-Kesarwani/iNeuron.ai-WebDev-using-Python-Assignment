n=int(input("Enter any number : "))
iterations = 1
number=1
while iterations<=10:
    if number%n==0:
        print(number)
        iterations+=1
    number+=1