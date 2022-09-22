# Define a function which calculates HCF of two numbers. 
# Define and apply a decorator to check whether two given numbers are co-prime or not.


def decor_check(result_func):
    def isCoPrime(a,b):
        min=a if a<b else b
        for i in range(1,min+1):
            if a%i==0 and b%i==0:
                hcf=i
        
        if hcf==1:
            print(a,",",b," are co-prime numbers!")
            result_func(a,b)
            
        else:
            print(a,",",b," are not co-prime numbers!")
            result_func(a,b)

    return isCoPrime


@decor_check
def hcf(a,b):
    min=a if a<b else b
    for i in range(1,min+1):
        if a%i==0 and b%i==0:
            hcf=i
    print("HCF of ",a,",",b,"is ",hcf)

hcf(7,49)