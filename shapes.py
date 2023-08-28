#Square
# for i in range(5):
#     for x in range(5):
#         print('x', end=' ')
#     print('')

#Right Triangle
# for i in range(5):
#     for x in range(i+1):
#         print('x', end=' ')
#     print(' ')

#Other Right Triangle
# for i in range(5):
#     for x in range(5-i):
#         print('x', end=' ')
#     print(' ')

#Equilateral Triangle
# for i in range(5):
#     for x in range(5-i):
#         print('', end=' ')
#     for x in range(i+1):
#         print('x', end=' ')
#     print(' ')

#Diamond
#For the top
for i in range(5):
    for x in range(5-i):
        print('', end=' ')
    for x in range(i+1):
        print('x', end=' ')
    print(' ')
#For the bottom
for i in range(5):
    for x in range(5-i):
        print('x ', end=' ')
    for x in range(i+1):
        print(' ', end=' ')
    print(' ')