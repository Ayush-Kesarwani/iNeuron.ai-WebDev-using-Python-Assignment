# Whether a file is closed or not

f=open("practice.txt","w")
f.write("My name is Ayush. I lives in Allahabad.")
f.close() 
print(f.closed)