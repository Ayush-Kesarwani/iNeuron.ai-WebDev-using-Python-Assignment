# Write a python program to reverse the tuple.

#one-way
a=("Java","Python","SQL","C")
print(a[::-1])

#second-way
b=()
for i in reversed(a):
    b=b+(i,)
print(b)