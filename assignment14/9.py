# Write a Python script to print indices of all occurrences of a given element in a given list.

element=input("Enter any element : ")

elist=["apple","boy","cat","boy","fox","deer","kangaroo","fox", "ship","ship"]

indexes=[]

for i in range(0,len(elist)):
    if element==elist[i]:
        indexes.append(i)
        
print(indexes)
