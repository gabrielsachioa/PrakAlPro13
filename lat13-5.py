def combination(n, r):
    if r == 0:
        return 1
    elif n < r:
        return "please enter n ≥ r ≥ 0"
    else:
        return n * combination(n - 1, r - 1) / r

print(combination(5, 0))
print(combination(1, 5))
print(combination(5, 2))