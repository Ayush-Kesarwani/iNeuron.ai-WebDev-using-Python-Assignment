decimal=int(input("Enter any decimal number : "))

binary=0
count=1
while decimal!=0:
    r=decimal%2
    binary=binary+(r*count)
    count*=10
    decimal//=2

print("Binary euqivalent = ",binary)