# 5. Print numbers from 1 to n after the recursive call.

def print_num(current, n):
    if current > n:
        return
    print(current)
    print_num(current+1, n)
    
print_num(1, 5)