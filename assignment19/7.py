# Write a python program to sum all the numbers in a list.

def sum(list):
    sumnum=0
    for i in list:
        sumnum+=i
    print(sumnum)
    
l=[1,2,3,4,5]
sum(l)