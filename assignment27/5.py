# Write a python script to handle multiple Exception in one try



div=0
try:
    a=int(input("Enter number to be divided : "))
    b=int(input("Enter number which divide : "))
    div=a/b
except ZeroDivisionError:
    print("Number not divided by 0!")
except ValueError:
    print("Value given is not applicable!")
finally:
    print(div)
    print("Program Closed!")



