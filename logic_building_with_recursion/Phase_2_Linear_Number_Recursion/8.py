# 8. Find the nth Fibonacci number using recursion. 

# 0 + 1 + 1 + 2 + 3

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return (fib(n-2) + fib(n-1)) ## fib 1 + fib 2 = 0 + 1

for i in range(1, 11):
    print(fib(i))
    