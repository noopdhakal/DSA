# 18. Check whether the given number is a prime number. 

n = 2
if n <= 0:
    print("Not a prime number")
else:
    i = 2
    is_prime = True
    while i < n:
        if n % i == 0:
            is_prime = False
            break      
        i += 1
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")
    
