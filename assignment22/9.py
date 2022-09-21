# Write a recursive python function to print octal of a given decimal number

def toOctal(n):
    if n==0:
        return 0
    return n%8+ 10*(toOctal(n//8))

print(toOctal(7))