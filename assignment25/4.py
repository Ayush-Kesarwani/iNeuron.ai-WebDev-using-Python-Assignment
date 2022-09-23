# Create a generator to produce squares of first N natural numbers

def n_square(n):
    a=1
    while n:
        yield a*a
        a+=1
        n-=1

for e in n_square(10):
    print(e,end=" ")
