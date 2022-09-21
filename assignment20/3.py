# Write a python program to create a function that prints the even numbers from a given list.

def even(list):
    for i in list:
        if(i%2==0):
            print(i,end=" ")

even([1,2,3,4,5,6,7,8,9])