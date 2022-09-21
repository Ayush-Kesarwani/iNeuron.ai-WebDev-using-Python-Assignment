# Write a Python script to find if “Python” is present in the set thisset = {"Java","Python", "Django"}

thisset = {"Java","Python", "Django"}

for i in thisset:
    if(i=="Python"):
        print("Python is present")
        break
else:
    print("Not present")
    