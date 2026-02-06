# 19. Print digits in words using recursion. 

words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
def digits_to_words(n):
    if n == 0: return
    digits_to_words(n // 10)
    print(words[n % 10], end=" ")

digits_to_words(345)