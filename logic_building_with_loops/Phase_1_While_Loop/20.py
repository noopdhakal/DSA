# 20. Find and print the sum of the Fibonacci series up to n terms.

n = 3
a, b = 0,1
count = 0
total = 0
while count < n:
    total += a
    c = a + b
    a = b
    b = c
    count += 1
print(total)



