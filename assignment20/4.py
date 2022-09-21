# Write a python program to create a function that checks whether a passed string is palindrome or not.

def isPalindrome(str):
    temp=str[::-1]
    if(temp==str):
        print("Palindrome string!")
    else:
        print("Not a palindrome string!")

isPalindrome("ayush")
