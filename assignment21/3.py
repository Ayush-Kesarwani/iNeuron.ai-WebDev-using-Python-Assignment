# Write a recursive python function to print first N odd natural numbers

def n_odd_number(n):
    if n==1:
        print(1)
    else:
        print((n*2)-1)
        n_odd_number(n-1)

n_odd_number(10)