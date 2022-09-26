# Write a python script to handle a ValueError

import math

num=int(input("Enter any number : "))

try:
    print(math.sqrt(num))
except ValueError:
    print("The value is not applicable to this method!")
except Exception:
    print("Something went wrong!")
finally:
    print("Program closed!")