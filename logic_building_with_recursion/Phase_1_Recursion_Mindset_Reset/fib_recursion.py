

# 0, 1, 1, 2, 3

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return (fib(n-2) + fib(n-1))

for i in range(1, 11):
    print(fib(i))