# 10. Print the Fibonacci series up to the required number of terms. 


#  0a 1b 1c 2
n = 5
a, b = 0, 1
for i in range(0, n + 1):
    print(a)
    c = a + b
    a = b
    b = c
