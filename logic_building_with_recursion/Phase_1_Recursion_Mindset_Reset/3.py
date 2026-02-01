# 3. Print numbers from 5 to 1 using recursion without loops.

def print_number(n):
    if n == 0:
        return
    print(n, end=" ")
    print_number(n-1)

print_number(5)