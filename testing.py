def mul(a, b):
    if b == 0:
        return 0
    return mul(a, b - 1) + a

print(mul(4, 5))