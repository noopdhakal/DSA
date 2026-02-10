def build_hash(arr):
    hash_arr = [0] * 13
    for x in arr:
        hash_arr[x] += 1
    return hash_arr


def process_queries(hash_arr):
    q = int(input())
    while q > 0:
        number = int(input())
        print(hash_arr[number])
        q -= 1


# ---- main logic ----
n = int(input())
arr = list(map(int, input().split()))

hash_arr = build_hash(arr)
process_queries(hash_arr)
