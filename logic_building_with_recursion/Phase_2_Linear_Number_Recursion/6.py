# Find the factorial of a number using recursion.

#  5 4 3 2 1 multiply

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
print(fact(3))