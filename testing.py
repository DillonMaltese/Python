def fibonnacci(a):
    if a == 1 or a == 2:
        return 1
    return fibonnacci(a - 2) + fibonnacci(a - 1)

print(fibonnacci(7 ))