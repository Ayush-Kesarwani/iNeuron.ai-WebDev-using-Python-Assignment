# Write a python program to create a function to check whether a string is an anagram or not

def isAnagram(str1,str2):
    if(sorted(str1)==sorted(str2)):
        print(str1," and ",str2," are anagram!")
    else:
        print(str1," and ",str2," are not anagram!")

isAnagram("spoon","noop")