decimal=int(input("Enter any decimal number : "))

octal=0
count=1
while decimal!=0:
    r=decimal%8
    octal=octal+(r*count)
    count*=10
    decimal//=8

print("Octal euqivalent = ",octal)