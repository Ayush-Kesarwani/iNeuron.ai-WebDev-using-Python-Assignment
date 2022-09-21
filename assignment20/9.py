# Write a python program to create a function to check whether a string is a pangram or not.

def isPangram(str):
    str=str.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    found=True
    for alpha in alphabet:
        if alpha not in str:
            found=False
            break
    if found==True:
        print(str," is Pangram")
    else:
        print(str," is not Pangram")
    
isPangram("the quick brown fox jumps over the lazy dog")
        
