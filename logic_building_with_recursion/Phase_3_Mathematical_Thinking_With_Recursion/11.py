# 1. Check whether a number is an Armstrong number. 

def sum_armstrong(n, p):
    if n == 0: return 0
    return (n % 10)**p + sum_armstrong(n // 10, p)