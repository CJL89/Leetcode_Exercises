arr = [17,18,5,4,6,1]

def replaceElements(arr):
    # Get elements in reverse
    maxValues = arr[-1]
    # Transform last element to -1
    arr[-1] = -1

    # Iterate thorugh the length of the array in reverse, ignore last 2 indexes
    for i in range(len(arr)-2, -1,-1):
        arr[i], maxValues = maxValues, max(maxValues, arr[i])
        print(arr[i], maxValues)
    return arr


print(replaceElements(arr))
