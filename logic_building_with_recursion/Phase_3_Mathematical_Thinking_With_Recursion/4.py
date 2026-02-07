# 4. Find the sum of the first n even numbers using recursion.

# 2, 4, 6, 8, ... , 2n

'''
Recursive Idea sum of first n even numbers = (n-1) + n 
'''


def sum_of_even(n):
    if n == 0:
        return 0
    return (2*n) + sum_of_even(n-1)
    
print(sum_of_even(4))
    
    