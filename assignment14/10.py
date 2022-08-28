# Write a python script to sort a list.

nlist=[34,56,21,34,89,67,54,33,98,10]

# sorting in ascending order 
for i in range(0,len(nlist)):
    for j in range(0,len(nlist)-1):
        if nlist[j]>nlist[j+1]:
            temp=nlist[j]
            nlist[j]=nlist[j+1]
            nlist[j+1]=temp

print(nlist)