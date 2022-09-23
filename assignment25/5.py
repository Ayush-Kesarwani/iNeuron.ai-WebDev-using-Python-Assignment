# Create a generator to produce first n terms of Fibonacci series

def n_fabo(n):
    a=0
    b=1
    while n:
        yield a
        a,b=b,a+b
        n-=1
    
for e in n_fabo(10):
    print(e, end=" ")