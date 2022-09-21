# Write a python program to create a function which expects an unknown number of arguments.

def numbers(*n):
    for i in n:
        print(i,end=" ")

numbers(1,2,3,4,5,6,7,8,9)

