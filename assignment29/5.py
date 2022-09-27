# Write a Python script to append list of city names in a file ‘cities.txt’

def appending(filename,text):
    with open(filename,"a") as f:
        f.write("\n")
        f.write(text)
        
appending("cities.txt","Aligarh")
appending("cities.txt","Agra")
appending("cities.txt","Mathura")
appending("cities.txt","Vrindavan")
appending("cities.txt","Mirzapur")
