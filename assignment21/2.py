# Write a recursive python function to print first N natural numbers in reverse order

def rev_natural(n):
    if n>0:
        print(n)
        rev_natural(n-1)

rev_natural(10)