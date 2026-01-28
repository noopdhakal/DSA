## 17. Print all prime numbers between 1 and 100. 

num = 2
while num <= 100:
    i, is_prime = 2, True

    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(num, end=" ")
    num += 1
