# Create a generator to produce first n even natural numbers

def n_even(n):
    a=2
    while n:
        yield a
        a+=2
        n-=1

for e in n_even(10):
    print(e, end=" ")