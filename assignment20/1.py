# Write a python program to create a function that takes a list and returns a new list with the original list's unique elements.

def unique(list):
    newlist=[]
    for i in list:
        if i not in newlist:
            newlist.append(i)
    
    print(list)
    print(newlist)

unique([1,2,3,2,1,3,4,5,3,2,3,4,5])