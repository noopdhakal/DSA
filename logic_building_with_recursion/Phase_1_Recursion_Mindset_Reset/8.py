# Print the current value of n during each recursive call.

def cur_value(n):
    if n == 0:
        return
    print(n)
    cur_value(n-1)
    

cur_value(5)

def trace_n(n):
    if n < 0:
        return
    print(f"Current n is: {n}")
    trace_n(n - 1)

trace_n(3)