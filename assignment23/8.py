# Create an endless iterator using generator method to produce Prime numbers

import math
from tkinter import Y

def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def primeGenerator():
    num=2
    while True:
        if isPrime(num):
            yield num 
        num+=1
        
it=primeGenerator()
l_prime=[]
while True:
    ans=input("Do you want to continue? Y/N : ")
    if ans=='Y' or ans=='y':
        l_prime.append(next(it))
    else:
        print(l_prime)
        break
