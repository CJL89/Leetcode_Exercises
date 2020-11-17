from itertools import groupby

arr = [2,1]
arr2 = [3,5,5]
arr3 = [0,3,2,1]
arr4 = [0,1,2,4,2,1]
arr5 = [0,1,2,3,4,8,9,10,11,12,11]


# def validMountainArray(arr):
#     if len(arr) <= 2:
#         return False
#     duplicates = [(k, len(list(g))) for k,g in groupby(arr)]
#     for i in duplicates:
#         if i[1] > 1:
#             return False
#     middle = arr.index(max(arr)) + 1
#     first = sorted(arr[:-middle])
#     last = sorted(arr[-middle:], reverse=True)
#     print(first, last)
#     print(arr[:-middle], arr[-middle:])
#     if arr[:-middle] == first and arr[-middle:] == last:
#         print(arr[:-middle] == first, arr[-middle:] == last)
#         return True
#     else:
#         return False

def validMountainArray(A):
    # i =ascending count - zero count
    # j = descending count
    # n = total len of array
    i, j, n = 0, len(A) - 1, len(A)
    while i + 1 < n and A[i] < A[i + 1]:
        i += 1
    while j > 0 and A[j - 1] > A[j]:
        j -= 1
    return 0 < i == j < n - 1

print(validMountainArray(arr5))
