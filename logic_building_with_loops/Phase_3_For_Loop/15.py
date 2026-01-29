# 15. Find the LCM (Least Common Multiple) of the given numbers. 

a, b = 12, 18
c, n = a, b
hcf = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        hcf = i

print("LCM", (c * n)//hcf)