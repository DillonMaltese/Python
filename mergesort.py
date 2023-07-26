from random import randint

def mergeSort(list):
    #Nothing needs to be sorted if list is length 1
    if len(list) == 1:
        return list

    #Middle finds and splits the list into left half + right half
    middle = len(list) // 2
    leftHalf = list[:middle]
    rightHalf = list[middle:]

    mergeSort(leftHalf)
    mergeSort(rightHalf)

    return merge(leftHalf, rightHalf)


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




list = [5, 2, 1, 4, 3, 7, 4, 8, 10, 9]
print(mergeSort(list))