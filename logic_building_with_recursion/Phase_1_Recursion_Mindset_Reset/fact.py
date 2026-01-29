
#5! = 5 * 4 * 3 * 2 * 1 
    # 5 * 4!
    # 5 * 4 * 3!
    # 5 * 4 * 3 * 2!

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

print(fact(5))