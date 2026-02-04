# Print "Start" only once and "End" only once using recursion.

def wrap_recursion(n):
    if n == 5:
        print("Start")
    if n == 0:
        print("End")
        return
    wrap_recursion(n-1)
    # print(n-1)

wrap_recursion(5)
