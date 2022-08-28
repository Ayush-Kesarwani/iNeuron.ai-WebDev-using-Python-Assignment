# Write a Python script to find the greatest number in a given list of numbers.

nlist=[45,32,89,65,43,12,10,65,76,43]

max=0

for i in nlist:
    if(i>max):
        max=i

print(max)