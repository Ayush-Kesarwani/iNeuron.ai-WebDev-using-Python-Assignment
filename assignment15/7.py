#  Write a python script to determine whether a string contains a specific substring

string=input("Enter any string : ")
sub=input("Enter any string to be checked : ")

if sub in string:
    print(sub," is present in ",string)
else:
    print(sub," is not present in ",string)