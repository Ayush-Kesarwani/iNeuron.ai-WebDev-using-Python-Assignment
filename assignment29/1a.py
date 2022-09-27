# Write a Python script to print the following status of a file:
# a. Whether a file is read only

f=open("practice.txt","w")
f.write("My name is Ayush. I lives in Allahabad.")
if f.mode=="r":
    print("Yes, file is in read only mode!")
else:
    print("No, file is not in read only mode!")
f.close()