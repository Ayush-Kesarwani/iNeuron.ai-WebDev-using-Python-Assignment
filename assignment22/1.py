# Write a recursive python function to calculate sum of first N natural numbers

def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)

print(sum(5))

