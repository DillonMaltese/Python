import numpy as np
all_coordinates = np.zeros((0, 2))

for y in range(2):
    for x in range(2):
        coordinate = np.array([[x,y]])

        # append
        all_coordinates = np.vstack((all_coordinates, coordinate))
        print(coordinate)
print(all_coordinates)