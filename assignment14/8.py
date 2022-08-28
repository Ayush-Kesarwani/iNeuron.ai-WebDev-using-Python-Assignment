# Write a Python script to print distinct elements along with their frequencies of occurrence in the list.

element=[1,2,3,4,5,2,3,4,5,3,4,5,4,5,5]

unique=[]

for i in range(0,len(element)-1):
    if element[i] not in unique:
        unique.append(element[i])

frequency=[]
for i in unique:
    count=0
    for j in element:
        if i==j:
            count=count+1
    frequency.append(count)

print("Element\t:\tFrequency")
for i in range(0,len(unique)):
    print(unique[i],"\t:\t",frequency[i])  