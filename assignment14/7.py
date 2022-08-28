# Write a Python script to remove all non int values from a list.

alist=["Java",2.4,"SQL",89,32,10,5.67,"Oracle","3.14",10]
blist=[]
for i in alist:
    if(type(i)==int):
        blist.append(i)
print(blist)