# Write a Python script to extract book data from a bookfile using pickle. Also print extracted book data.

import pickle

f=open('bookfile','rb')
s=pickle.load(f)
for key in s:
    print(key," : ",s[key])

f.close()