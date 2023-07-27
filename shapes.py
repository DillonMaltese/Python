#Square
# for i in range(5):
#     for x in range(5):
#         print('x', end = ' ')
#     print('')


#Right Triangle
# for i in range(5):
#     for x in range(i+1):
#         print('x', end = ' ')
#     print('')

#Equilateral
# for i in range(5):
#     for x in range(5 - i - 1):
#         print(' ', end = '')
#     for y in range(i + 1):
#         print('x ', end = '')
#     print('')


#Diamond
# for i in range(5):
#     for x in range(5 - i - 1):
#         print(' ', end = '')
#     for y in range(i + 1):
#         print('x ', end = '')
#     print('')

# for i in range(5):
#     for y in range(i + 1):
#         print(' ', end = '')
#     for x in range(5 - i - 1):
#         print('x ', end = '')
#     print('')


#Hollow Diamond
for i in range(5):
    for x in range(5 - i - 1):
        print(' ', end = '')
    for y in range(i + 1):
        print('x ', end = '')
    print('')

for i in range(5):
    for y in range(i + 1):
        print(' ', end = '')
    for x in range(5 - i - 1):
        print('x ', end = '')
    print('')