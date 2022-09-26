# Write a python script to implemented a nested Try Except block


division=0
try:
    a=int(input("Enter a number to be divided : "))
    b=int(input("Enter a number which divide : "))
    try:
        division=a/b
        if a<0 or b<0:
            raise ArithmeticError
    except ZeroDivisionError:
        print("Number can not be divided by 0!")
    else:
        print("Division = ",division)
except ValueError:
    print("Value given is not valid!")
except ArithmeticError:
    print("Error is occurred!")
except NameError:
    print("Variable use in the operated statement is not valid!")
finally:
    print("Program Closed!")

