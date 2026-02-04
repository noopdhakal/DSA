# Print odd numbers from 1 to n using recursion.

def print_odd(n):
    if n == 0:
        return 
    print_odd(n-1)
    if n % 2 !=0: print(n, end=" ")

print_odd(10)