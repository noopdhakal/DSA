# 24. Print all factors of the given number. 

n = 8 # 1 3 2
i = 1
while (i < n):
    if n % i == 0:
        print(i, end=" ")
    i += 1


