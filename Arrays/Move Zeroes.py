arr = [0,1,0,3,12]

def moveZeroes(arr):
    if len(arr) == 0:
        return arr

    pos = 0

    if 0 in arr:
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[pos], arr[i] = arr[i], arr[pos]
                pos += 1

    return arr

print(moveZeroes(arr))
