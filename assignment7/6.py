str = input("Enter any string : ")
multi_string=False
for i in range(len(str)):
    if str[i]==' ' and str[i+1].isalpha()==True:
        print("Multiword String")
        multi_string=True
        break
    else:
        continue
if multi_string==False:
    print("Singleword string")