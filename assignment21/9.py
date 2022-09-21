# Write a recursive python function to print first N multiples of a given number.

def multiples(num, n):
    if n==1:
        print(num,"*",n,"=",num*n)
    else:
        multiples(num,n-1)
        print(num,"*",n,"=",num*n)

multiples(2,5)