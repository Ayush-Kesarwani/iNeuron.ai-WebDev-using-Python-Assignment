# Write a python program to create a function that accepts a string and calculate the number of upper case letters and lower case letters.

def case_count(str):
    lower=0
    upper=0
    for i in str:
        if i>='a' and i<='z':
            lower+=1
        if i>='A' and i<='Z':
            upper+=1
    
    print("Number of lowercase letters : ",lower)
    print("Number of uppercase letters : ",upper)

case_count("Ayush Kesarwani is a good boy!")