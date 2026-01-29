
# 2 5 , 2 * 2 4 , 2 * * 2 *3

def power(base, a):
    if a == 0:
        return 1
    return  base * power(base, a-1)

print(power(2, 2))