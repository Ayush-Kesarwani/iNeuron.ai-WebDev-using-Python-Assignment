# Write a python script to reverse a String. (“iNeuron”)

s="iNeuron"

# one-way : 
reverse=""
for i in s:
    reverse=i+reverse
print(reverse)

# second-way :
reverse=""
for i in range(len(s)-1,-1,-1):
    reverse+=s[i]
print(reverse)

