## 11. Find and print the sum of the Fibonacci series. 


n = 8
a, b = 0, 1
for i in range(n):
    c = a + b
    a = b
    b = c
print(a)