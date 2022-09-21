# Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.

roll_no=[1,2,3,4,5]
name=["Ayush","Jatin","Dhruv","Samarth","Sarthak"]

dict={}
for i in roll_no:
    dict[i]=name[i-1]

print(dict)