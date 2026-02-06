# 15. Convert decimal to binary using recursion. 

# 8421 --> 0010

def dec_to_bin(n):
    if n == 0:
        return ""
    return dec_to_bin(n//2) + str(n%2)

print(dec_to_bin(13))