# Write a python program to create a function to find the Min of three numbers.

def min(a,b,c):
    if(a<b and a<c):
        print(a, " is minimum.")
    elif(b<c):
        print(b," is minimum.")
    else:
        print(c," is minimum.")

min(67,34,5)