# 8. Find the maximum and minimum digit in a given number. 

def max_num(n):
    if n < 10: return n
    return max(n%10, max_num(n//10))

def get_min(n):
    if n < 10: return n
    return min(n % 10, get_min(n // 10))