# Count digits in a number using recursion.
# 123 ==> 123 % 10 --> 3 

def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n//10)


print(count_digits(123))