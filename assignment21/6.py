# Write a recursive python function to print first N even natural numbers in reverse order.

def n_even_numbers(n):
    if n==1:
        print(2)
    else:
        n_even_numbers(n-1)
        print(n*2)
        

n_even_numbers(5)