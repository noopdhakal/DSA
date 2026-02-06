# 17. Print digits one by one using recursion. 

def digits_one_one(n):
    if n == 0:
        return 
    digits_one_one(n//10)
    print(n%10)

digits_one_one(1234)