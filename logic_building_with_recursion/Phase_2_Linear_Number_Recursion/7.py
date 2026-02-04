# Calculate xⁿ (power of a number) using recursion. 

# 2 * 4 , 2 * 3

2 * 2**2 * 2

def power_number(x,n):
    if n == 0:
        return 1 
    return x * power_number(x, n - 1)
print(power_number(2, 3))
