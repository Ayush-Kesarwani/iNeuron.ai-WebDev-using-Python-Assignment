age=int(input("Enter your age : "))

if age<10:
    print("Kid")
elif age>=10 and age<20:
    print("Teen")
elif age>=20 and age<40:
    print("Young")
elif age>=40 and age<60:
    print("Experienced")
elif age>=60:
    print("Senior Citizen")
else:
    print("Inavlid Age")