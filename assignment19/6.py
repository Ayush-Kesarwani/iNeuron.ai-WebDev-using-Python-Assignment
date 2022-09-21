# Write a python program to create a function that finds a maximum of four numbers.

def max(a,b,c,d):
    if(a>b and a>c and a>d):
        print(a,"is greater!")
    elif(b>c and b>d):
        print(b," is greater!")
    elif(c>d):
        print(c," is greater!")
    else:
        print(d," is greater!")

max(34,65,12,21)