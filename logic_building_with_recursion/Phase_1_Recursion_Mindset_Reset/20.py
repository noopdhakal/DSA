# 20. Count zeros in a number using recursion.

def count_zeros(n):
    if n == 0: return 0
    count = 1 if n%10 == 0 else 0
    return count + count_zeros(n//10)

print(count_zeros(10002))