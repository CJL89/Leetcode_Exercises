array = [9, -2, -9, 11, 56, -12, -3]

def squaredEvenIndex(arr):
    for i, n in enumerate(arr):
        if i % 2 == 0:
            arr[i] = arr[i] ** 2
    return arr


print(squaredEvenIndex(array))
