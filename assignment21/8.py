# Write a recursive python function to print cubes of first N natural numbers

def square(n):
    if n==1:
        print(1)
    else:
        square(n-1)
        print(n*n*n)

square(5)