# Write a recursive python function to print first N natural numbers.

def natural(n):
    if n>0:
        natural(n-1)
        print(n)

natural(10)