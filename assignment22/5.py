# Write a recursive python function to calculate sum of cubes of first N natural numbers

def sum_square(n):
    if n==1:
        return n*n*n
    return n*n*n+sum_square(n-1)

print(sum_square(5))