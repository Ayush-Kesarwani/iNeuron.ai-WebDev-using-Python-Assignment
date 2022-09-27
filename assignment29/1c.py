# Which file opening mode is used

f=open("practice.txt","r+")
f.write("My name is Ayush. I lives in Allahabad.")
print(f.mode)
f.close()