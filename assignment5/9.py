list=["a","e","i","o","u"]
str=input("Enter any single string : ")

for i in str:
    if(i not in list):
        print(i," ",end="")
    else:
        continue
    
