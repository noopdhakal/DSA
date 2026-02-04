# Find the sum of first n natural numbers using recursion.

count = 0
def sum_natural(n):
    global count 
    if n == 0:
        return
    sum_natural(n-1)
    count += n 
    return count

print(sum_natural(5))

# 5 + 4 + 3 + 2 + 1

def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n-1)

print(sum_n(5))