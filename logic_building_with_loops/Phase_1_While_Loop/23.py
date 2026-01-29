# 23. Print all numbers between a and b that are divisible by 7.

a = 1 
b = 21
while a <= b:
    if a % 7 == 0:
        print(a)
    a += 1