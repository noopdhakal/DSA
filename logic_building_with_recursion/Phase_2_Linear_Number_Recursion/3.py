# Print even numbers from 1 to n using recursion.

# 2 4 6

def even_num(n):
    if n == 0:
        return
    even_num(n-1)
    if n % 2 == 0: print(n, end= " ")
    
even_num(10)
    
    