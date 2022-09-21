# Write a python program to Sort a tuple of tuples by the second item.

tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))

l=len(tuple1)

for i in range(0,l):
    for j in range(0,l-i-1):
        if(tuple1[j][1]>tuple1[j+1][1]):
            temp=tuple1[j]
            tuple1[j]=tuple1[j+1]
            tuple1[j+1]=temp
print(tuple1) 
