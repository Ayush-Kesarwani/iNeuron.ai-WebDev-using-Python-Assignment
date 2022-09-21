# Write a python program to multiply all the numbers in a list

def mul(list):
    mulnum=1
    for i in list:
        mulnum*=i
    print(mulnum)
    
l=[1,2,3,4,5]
mul(l)