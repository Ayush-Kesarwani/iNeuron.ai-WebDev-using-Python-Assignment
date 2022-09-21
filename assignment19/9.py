# Write a python program to create a function to check whether a number falls in a given range.

def found(min_range,max_range,num):
    if num in range(min_range,max_range+1):
        print(num," falls in range!")
    else:
        print(num," not falls in range!")

found(5,10,8)