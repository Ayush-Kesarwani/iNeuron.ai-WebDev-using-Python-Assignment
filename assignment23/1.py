# Use iter and next method to access all the elements of a given set using while loop

set={1,2,3,4,5,6}
it=iter(set)

while True:
    try:
        print(next(it), end=" ")
    except StopIteration:
        break
