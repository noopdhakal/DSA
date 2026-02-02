# Print numbers from 1 to n before the recursive call. 

def print_num(start, n):
    if n == 0:
        return
    print(n)
    print_num(start, n-1)
print_num(1,5)