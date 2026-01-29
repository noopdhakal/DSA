# 18. Print all numbers between a and b that are divisible by 7. 

a, b = 1, 23
for i in range(a, b):
    if i % 7 == 0:
        print(i)
