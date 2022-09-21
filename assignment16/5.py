# Write a python program to check if all items in the tuple are the same.

a=("Java","Python","C++","C")
found=False
for i in a:
    for j in a:
        if i!=j:
            found=True
            break

if found==False:
    print("All items in tuples are same")
else:
    print("All items in tuples are not same")