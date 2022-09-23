# Create a generator to produce first n odd natural numbers

def n_odd(n):
    a=1
    while n:
        a+=2
        yield a
        n-=1

for e in n_odd(10):
    print(e, end=" ")
