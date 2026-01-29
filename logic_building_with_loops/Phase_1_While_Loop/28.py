# 28. Find the smallest digit in the given number. 

n = 123
smallest = 9 #highest possible digit
while n > 0:
    last_digit = n % 10
    if last_digit < smallest:
        smallest = last_digit
    n //=10
print(smallest)
