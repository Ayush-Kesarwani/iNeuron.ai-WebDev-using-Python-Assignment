print("Type 1 - To check for isosceles triangle.")
print("Type 2 - To check for right angle triangle.")
print("Type 3 - To check for equilateral triangle.")
print("Type 4 - To exit.")

choice = int(input("Enter your choice : "))

if choice==4:
    print("Program closed!")

elif choice>4 or choice<0:
    print("Invalid choice!")

else:
    s1=int(input("Enter of value of length od side 1 of triagle : "))
    s2=int(input("Enter of value of length od side 1 of triagle : "))
    s3=int(input("Enter of value of length od side 1 of triagle : "))

    if choice==1:
        if s1==s2 or s2==s3 or s1==s3:
            print("This is an isoceles triangle.")
        else:
            print("This is not an isoceles triangle.")
    elif choice==2:
        if (s1**2 + s2**2) == s3**2:
            print("This is a right-angled triangle.")
        else:
            print("This is not a right-angled triangle.")
    elif choice==3:
        if s1==s2==s3:
            print("This is an equilateral triangle.")
        else:
            print("This is not an equilateral triangle.")
