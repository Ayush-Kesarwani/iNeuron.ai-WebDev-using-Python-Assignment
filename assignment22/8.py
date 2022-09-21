# Write a recursive python function to print binary of a given decimal number.

def toBinary(n):
    if n==0:
        return 0
    return n % 2 + 10*(toBinary(n//2))

print(toBinary(5))