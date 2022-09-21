# Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not.
import math
def isPrime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if(num%i==0):
            print(num," is not Prime!")
            break
    else:
        print(num," is Prime!")

isPrime(91)