
def count_number(n):
    if n < 10: ## less than 10 so
        return 1
    return 1 + count_number(n // 10)

print(count_number(567894))