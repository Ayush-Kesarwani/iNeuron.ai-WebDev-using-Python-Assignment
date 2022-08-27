n = int(input("Enter any number : "))

sum=0
for i in range(1, n+1):
    sum+=i*i

print(f"Sum of first {n} natural numbers is {sum}")