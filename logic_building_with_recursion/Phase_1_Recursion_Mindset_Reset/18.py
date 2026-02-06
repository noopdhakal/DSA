# 18. Print digits in reverse order using recursion. 

def digits_one_one(n):
    if n == 0:
        return 
    print(n%10, end=" ")
    digits_one_one(n//10)
    

digits_one_one(1234)