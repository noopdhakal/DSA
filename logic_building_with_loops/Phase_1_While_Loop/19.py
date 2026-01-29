# 19. Print the Fibonacci series up to n terms.

# 0 + 1 + 1 + 2 + 3
n = 10
a, b = 0, 1
count = 0
while count < n:
    print(a, end=' ')
    c = a + b
    a = b
    b = c
    count += 1
 