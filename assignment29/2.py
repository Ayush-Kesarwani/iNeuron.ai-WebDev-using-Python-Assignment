# Write a Python script to create a new file ‘myfile.txt’ and store user entered text.

text=input("Enter any text you want to save in the file : ")

with open("myfile.txt","w") as f:
    f.write(text)