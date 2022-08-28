# Write a python script to check if a string contains only characters of the alphabet.

s=input("Enter any string : ")
found=False
for i in s:
    if (ord(i)<65 or ord(i)>90) and (ord(i)<97 or ord(i)>122):
        print("No, string does not contain only alphabets!")
        found=True
        break
if found==False:
    print("Yes, string contains only alphabets!")