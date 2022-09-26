# Write a python script to create a calculator with 4 basic operations, and handle a
# maximum number of exceptions.

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
        
        print("Addition = ",add)

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
        
        print("Substraction = ",sub)

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
        
        print("Multiplication = ",multiply)

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
        
        print("Division = ",division)




print("Type 1 - for adding numbers.")
print("Type 2 - for substracting numbers.")
print("Type 3 - for multiplicating numbers.")
print("Type 4 - for dividing numbers.")

choice=0
try:
    choice=int(input("Enter your choice : "))
except ValueError:
    print("Value given is not valid and should only number!")
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