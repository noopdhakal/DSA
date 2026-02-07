# Count the number of prime digits in a given number. 

def count_prime(n):
    if n == 0: return 0
    digit = n % 10
    is_p = 1 if digit in [2, 3, 5, 7] else 0
    return is_p + count_prime(n//10)
    
print(count_prime(59234))