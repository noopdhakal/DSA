# 1. Find the GCD of two numbers using Euclid’s algorithm. 


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

print(gcd(48, 6))