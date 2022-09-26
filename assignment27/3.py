# Write a python script to handle the ArithmeticError

a=int(input("Enter any number : "))

try:
    div=a/0
except ArithmeticError:
    print("Number can not be divisible by 0!")
finally:
    print("Program Closed............!")
