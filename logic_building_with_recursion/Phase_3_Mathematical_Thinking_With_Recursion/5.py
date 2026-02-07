# 5. Find the sum of the first n odd numbers using recursion. 



def odd_print(n):
    if n == 1:
        return 1
    return (2*n - 1) + odd_print(n-1)

print(odd_print(3))
