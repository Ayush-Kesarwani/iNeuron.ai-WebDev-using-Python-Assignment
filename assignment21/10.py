# Write a recursive python function to print a number in reverse order.
rev_num=0
def reverse(num):
    global rev_num
    if num>0:
        d = num % 10  
        rev_num = (rev_num * 10) + d 
        reverse(num//10)
    return rev_num
    

num=reverse(12345)
print(num)