# Define a function which takes lengths of three sides of a triangle as arguments and
# display the perimeter or triangle. Define and apply a decorator which checks for the
# validity of the triangle on the basis of lengths of the side. This makes the perimeter to
# be displayed when the triangle can exist with the given lengths of the sides.

#  A triangle is valid if sum of its two sides is greater than the third side. 
# If three sides are a, b and c, then three conditions should be met
# 1.a + b > c 
# 2.a + c > b 
# 3.b + c > a

def decor_check(result_func):
    def validity(a,b,c):
        if(a+b>c and a+c>b and b+c>a):
            print("Valid Triangle!")
            result_func(a,b,c)
        else:
            print("Invalid Triangle!")
    return validity

@decor_check
def perimeter(a,b,c):
    print("Perimeter of Triangle = ",(a+b+c))

perimeter(7,10,5)