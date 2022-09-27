# Write a Python script to read the above created file ‘myfile.txt’ and display content on the console.

def reading(filename):
    try:
        with open(filename,"r") as f:
            text=f.read()
            print(text)
    except FileNotFoundError:
        print("File not found!")
    finally:
        f.close()

reading("myfile.txt")
