# Create a generator to produce first n prime numbers
import math

def isPrime(num):
    for i in range(2,num):
        if num%2==0:
            return False
    return True

def primeGenerator(n):
    num=2
    while n:
        if isPrime(num):
            yield num 
            n-=1
        num+=1
        

for e in primeGenerator(5):
    print(e, end=" ")
