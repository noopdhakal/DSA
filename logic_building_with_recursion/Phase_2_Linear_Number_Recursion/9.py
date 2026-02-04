# Print Fibonacci series up to n terms using recursion.


def fib(n):
    if n <= 1: return n
    return fib(n - 1) + fib(n - 2)

def print_fib_series(n, current=0):
    if current == n: return
    print(fib(current), end=" ")
    print_fib_series(n, current + 1)