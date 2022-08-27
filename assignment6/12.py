number=input("Enter complex number : ")
number=complex(number)
real=number.real
imaginary=number.imag
if real>imaginary:
    print(real)
elif real==imaginary:
    print("equal")
else:
    print(imaginary)