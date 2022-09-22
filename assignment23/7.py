# Create an endless iterator using generator method to produce terms of Fibonacci series

def n_fabo():
    a=0
    b=1
    while True:
        yield a
        a,b=b,a+b

it=n_fabo()
l_fabo=[]
while True:
    ans=input("Do you want to continue? Y/N : ")
    if ans=='Y' or ans=='y':
        l_fabo.append(next(it))
    else:
        print(l_fabo)
        break
