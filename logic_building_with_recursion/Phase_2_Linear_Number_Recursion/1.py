# Print numbers from 1 to n using recursion. 

def print_num(n):
    if n == 0:
        return
    print(n, end=" ")
    print_num(n-1)
    # print(n, end=" ")
print_num(10)