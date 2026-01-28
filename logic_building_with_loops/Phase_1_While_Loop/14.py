## Find and print the sum of digits of the given number.

n = 1234
last_digit = 0
while (n > 0):
    last_digit += n % 10
    n //= 10

print(last_digit)