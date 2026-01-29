# 29. Find the largest digit in the given number.

n = 123
highest = 0
while n > 0:
    digit = n % 10
    if digit > highest:
        highest = digit
    n //= 10
print(highest)