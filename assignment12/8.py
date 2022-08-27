n=int(input("Enter any number : "))
first,second=0,1
if n==1:
    print(first)
else:
    for i in range(0,n):
        print(first)
        third=first+second

        first=second
        second=third
    