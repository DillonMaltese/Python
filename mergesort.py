from random import randint

def mergeSort(list):
    #Nothing needs to be sorted if list is length 1
    if len(list) == 1:
        return list

    #Middle finds and splits the list into left half + right half
    middle = len(list) // 2
    leftHalf = list[:middle]
    rightHalf = list[middle:]

    left = mergeSort(leftHalf)
    right = mergeSort(rightHalf)

    return merge(left, right)


def merge(left, right):
    merged = []
    leftIndex = 0
    rightIndex = 0

    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] <= right[rightIndex]:
            merged.append(left[leftIndex])
            leftIndex += 1

        else:
            merged.append(right[rightIndex])
            rightIndex += 1

    merged.extend(left[leftIndex:])
    merged.extend(right[rightIndex:])

    return merged




list = [5, 2, 1, 4, 7, 9, 19, 45, 32, 10, 9, 324, 546, 213, 435, 546, 78, 32, 21, 324, 345, 321, 12, 123234]
print(mergeSort(list))