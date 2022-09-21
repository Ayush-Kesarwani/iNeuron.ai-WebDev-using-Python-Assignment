# Write a recursive python function to print first N even natural numbers.

def n_even_numbers(n):
    if n==1:
        print(2)
    else:
        print(n*2)
        n_even_numbers(n-1)

n_even_numbers(5)