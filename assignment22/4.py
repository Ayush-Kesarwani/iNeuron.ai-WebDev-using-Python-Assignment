# Write a recursive python function to calculate sum of squares of first N natural numbers

def sum_square(n):
    if n==1:
        return n*n
    return n*n+sum_square(n-1)

print(sum_square(5))