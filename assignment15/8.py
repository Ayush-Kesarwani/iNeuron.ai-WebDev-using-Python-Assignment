#  Write a python script to check if a string contains only numbers.

s=input("Enter any string : ")
found=False
for i in s:
    if ord(i)<48 or ord(i)>57:
        print("No, string does not contain only numbers!")
        found=True
        break
if found==False:
    print("Yes, string contains only numbers!")
