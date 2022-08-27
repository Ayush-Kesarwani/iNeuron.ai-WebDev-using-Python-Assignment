number = int(input("Enter your number : "))

if number%2==0:
    print("Saurabh Shukla")
elif number%2!=0 and number<0:
    print("Prateek Jain")
elif number%2!=0 and number>0:
    print("Aditya Choudhary")
else:
    print("Invalid number inputed!")