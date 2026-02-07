# 3. Find nCr using Pascal’s relation recursively


def nCr(n, r):
    if r == 0 or r == n:
        return 1
    return nCr(n - 1, r - 1) + nCr(n - 1, r)