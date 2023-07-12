# rows, cols = (7, 7)
# print("The o will represent you and the x represents the enemy. Move around to find the hidden items")
# roomPic = [['_'] * cols]*rows
# for i in range(len(roomPic)):
#     for j in range(len(roomPic[i])):
#         print(roomPic[i][j], end = '')

# Get the size of the 2D array from the user
size = int(input("Enter the size of the 2D array: "))

# Create the 2D array
array_2d = [[0] * size for _ in range(size)]

# Print the 2D array
for row in array_2d:
    print(row)