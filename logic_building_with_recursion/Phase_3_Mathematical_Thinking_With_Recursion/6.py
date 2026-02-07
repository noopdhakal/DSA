# 6. Check whether a number is prime using recursion.

def prime(n, i=2):
    if n<=2: return n == 2
    if n % i == 0: return False
    return prime(n, i+1)

print(prime(3))