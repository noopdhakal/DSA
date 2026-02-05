# 12. Find the product of digits of a number using recursion. 

def find_product(n):
    if n == 0:
        return 1
    return (n%10) * find_product(n//10)

print(find_product(1234))