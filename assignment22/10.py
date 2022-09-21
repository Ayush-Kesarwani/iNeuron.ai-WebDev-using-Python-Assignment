# Write a recursive python function to find the Nth term of the Fibonacci series.

def fabo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fabo(n-1)+fabo(n-2)

print(fabo(5))