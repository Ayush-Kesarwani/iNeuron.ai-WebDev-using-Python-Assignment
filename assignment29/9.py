# Write a Python script to store book data in a file. Book data is in the form of a
# dictionary in which book name is the key and price is its value. Use pickle to store
# data into a file (say bookfile)

import pickle

bookinfo={"English":200, "Maths":250, "Physics":240, "Chemistry":300, "Hindi":150}

f=open('bookfile','ab')
pickle.dump(bookinfo,f)
f.close()