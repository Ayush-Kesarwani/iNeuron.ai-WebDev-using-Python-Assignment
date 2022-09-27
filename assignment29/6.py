# Write a Python script to search whether a particular city is there in the file ‘cities.txt’ or not

def search(filename,text):
    try:
        with open(filename,"r") as f:
            content = f.read()
            if text in content:
                return True
            else:
                return False
    except FileNotFoundError:
        print("File not found!")


city=input("Enter city name : ")

if search("cities.txt",city)==True:
    print(city," is present in the file!")
else:
    print(city," is not present in the file!")