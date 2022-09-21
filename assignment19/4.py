# Write a python program to create a function which expects kwargs arguments.

def func(**kwargs):
    for i in kwargs:
        print(kwargs[i])

def func(**kwargs):
    print(kwargs)

func(a="Ayush",b="Jatin")