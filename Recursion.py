def add(start, num):
    if num == 0:
        return start
    return add(start + num, num - 1)


#print(add(0, 5))

def fibonacci(a):
    if a == 1 or a == 2:
        return 1
    return fibonacci(a - 2) + fibonacci(a - 1)

print(fibonacci(7))