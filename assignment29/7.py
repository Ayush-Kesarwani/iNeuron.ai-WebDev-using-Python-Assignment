# Write a Python script to count the number of Python keywords occurring in a python source file.
import keyword

def count_keywords(filename):
    count=0
    try:
        with open(filename,"r") as f:
            for line in f.readlines():
                str=line.split(' ')
                for i in keyword.kwlist:
                    if i in str:
                        count+=1
        return count
    except FileNotFoundError:
        print("File not found!")

n=count_keywords("myfile.txt")
print(n," number of keywords of python present in the source file.")