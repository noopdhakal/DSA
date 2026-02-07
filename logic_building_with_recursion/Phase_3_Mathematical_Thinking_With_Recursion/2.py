# 2. Find the LCM of two numbers using recursion.

def hcf(a, b):
    if b == 0:
        return a 
    return hcf(b, a%b)

a, b = 48, 18
hcf = hcf(a, b)
lcm = (a*b)//hcf
print(lcm)