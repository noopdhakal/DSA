# 16. Convert decimal to octal using recursion. 


# 8421--> 1100 --> 12
def dec_to_octal(n):
    if n == 0:
        return ""
    return dec_to_octal(n//8) + str(n%8)

print(dec_to_octal(12))