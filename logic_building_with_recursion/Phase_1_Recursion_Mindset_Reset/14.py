# 14. Check if a number is a palindrome using recursion. 

def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n//10, rev * 10 + n % 10)

def is_palindrome(n):
    return n == reverse_number(n)


print(is_palindrome(121))