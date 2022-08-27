year=int(input("Enter year : "))

if year%400==0 and year%100==0:
    print("Century Leap Year")
elif year%4==0 and year%100!=0:
    print("Non Century Leap Year")
elif year%400!=0 and year%100==0:
    print("Century Non Leap Year")
elif year%400!=0 and year%100!=0:
    print("Non Century Non Leap Year")
else:
    print("Invalid Year")