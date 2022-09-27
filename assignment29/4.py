# Write a Python script to store a list of city names in a file ‘cities.txt’

def writing(filename,text):
    with open(filename,"w") as f:
        f.write(text)

writing("cities.txt","Prayagraj\nKanpur\nVaranasi\nMeerut\nLucknow")

