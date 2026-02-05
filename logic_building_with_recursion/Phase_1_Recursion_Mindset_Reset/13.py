# 13. Reverse a number using recursion. 

# 123 ==> 3 * 100... rev(12, 3)

# rev (1, 3 * 10 + 2).. so on 

def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n//10, rev * 10 + n % 10)

print(reverse_number(123))