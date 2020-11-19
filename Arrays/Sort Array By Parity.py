arr = [3,1,2,4]

def sortArrayByParity(arr):
    if len(arr) == 0:
        return arr

    pos = 0

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[pos], arr[i] = arr[i], arr[pos]
            # print(arr[pos], arr[i])
            pos += 1

    return arr

print(sortArrayByParity(arr))
