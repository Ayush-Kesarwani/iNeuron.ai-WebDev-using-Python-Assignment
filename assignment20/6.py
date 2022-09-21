# Write a python program to create a function and print a list where the values are square of numbers between 1 and 30.

def square():
    list=[]
    for i in range(1,30):
        if(i*i<30):
            list.append(i*i)
        else:
            break
    print(list)
square()