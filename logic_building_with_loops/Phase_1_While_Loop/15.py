# 15. Check whether the given number is an Armstrong number. 


# 153 1634 Armstrong number

n = 153
order = len(str(n))
sum, arm = 0,n 
while ( n > 0):
    last_digit = n % 10
    sum += last_digit ** order
    n //= 10
if sum == arm:
    print("Armstrong Number")
else: 
    print("Not Armstrong Number")
