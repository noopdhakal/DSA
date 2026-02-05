# 11. Find the sum of digits of a number using recursion.

# 123 -> 3 + sum_of_digits(12)

# 123 --> 3 
def sum_of_digits(n):
    if n == 0: return 0
    return (n%10) + sum_of_digits(n//10)

print(sum_of_digits(123))