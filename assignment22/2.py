# Write a recursive python function to calculate sum of first N odd natural numbers

def sum_odd(n):
    if n==1:
        return 1
    return ((n*2)-1)+sum_odd(n-1)

sum=sum_odd(5)
print(sum)