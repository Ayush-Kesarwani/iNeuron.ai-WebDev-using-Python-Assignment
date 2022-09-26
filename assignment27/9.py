# Write a python script to raise value error.


from multiprocessing.sharedctypes import Value
from tokenize import Name


class Calculator:
    def add():
        add=0
        try:
            a=int(input("Enter 1st number : "))
            b=int(input("Enter 2nd number : "))
            add=a+b
        except ValueError:
            print("Value given is not valid!")
        except ArithmeticError:
            print("Error is occurred!")
        except NameError:
            print("Variable use in the operated statement is not valid!")
        else:
            print("Addition = ",add)
        finally:
            print("Program Closed!")

    def substract():
        sub=0
        try:
            a=int(input("Enter 1st number : "))
            b=int(input("Enter 2nd number : "))
            sub=a-b if a>b else b-a
        except ValueError:
            print("Value given is not valid!")
        except ArithmeticError:
            print("Error is occurred!")
        except NameError:
            print("Variable use in the operated statement is not valid!")
        else:
            print("Substraction = ",sub)
        finally:
            print("Program Closed!")

    def multiply():
        multiply=0
        try:
            a=int(input("Enter 1st number : "))
            b=int(input("Enter 2nd number : "))
            multiply=a*b
        except ValueError:
            print("Value given is not valid!")
        except ArithmeticError:
            print("Error is occurred!")
        except NameError:
            print("Variable use in the operated statement is not valid!")
        else:
            print("Multiplication = ",multiply)
        finally:
            print("Program Closed!")

    def division():
        division=0
        try:
            a=int(input("Enter 1st number : "))
            b=int(input("Enter 2nd number : "))
            division=a/b
        except ZeroDivisionError:
            print("Number can not be divided by 0!")
        except ValueError:
            print("Value given is not valid!")
        except ArithmeticError:
            print("Error is occurred!")
        except NameError:
            print("Variable use in the operated statement is not valid!")
        else:
            print("Division = ",division)
        finally:
            print("Program Closed!")




print("Type 1 - for adding numbers.")
print("Type 2 - for substracting numbers.")
print("Type 3 - for multiplicating numbers.")
print("Type 4 - for dividing numbers.")


choice=0
try:
    choice=int(input("Enter your choice : "))
    if choice<1 or choice>4:
        raise ValueError()
except ValueError:
    print("Value given is not valid and should only from the listed choice!")
else:
    print("You are good to go.............")




if choice==1:
    Calculator.add()
elif choice==2:
    Calculator.substract()
elif choice==3:
    Calculator.multiply()
elif choice==4:
    Calculator.division()
else:
    print("Invalid Choice!")