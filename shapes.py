#Square
for i in range(5):
    for x in range(5):
        print('x', end = ' ')
    print('')


#Right Triangle
for i in range(5):
    for x in range(i+1):
        print('x', end = ' ')
    print('')

#Equilateral

for i in range(5):
    for x in range(i - 1):
        print('x ', end = '')
    for y in range(i - 2):
        print('x ' end = ' ')
    print('')