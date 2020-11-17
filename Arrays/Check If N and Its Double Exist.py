import collections

arr3 = [10,2,5,3]
arr2 = [3,1,7,11]
arr4 = [7,1,14,11]
arr5 = [-20,8,-6,-14,0,-19,14,4]
arr = [0,0]

# count = []
#
# for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#         n = arr[i] / 2
#         ii = bool()
#         if n in arr:
#             ii = bool(n)
#             print(ii)
#         elif ii != True:
#             print(False)


# count = collections.Counter(arr)
#
# for i in arr:
#     if i * 2 in arr and i * 2 != 0 or i.count(0) > 1:
#         print(True)
#     else:
#         print(False)

if arr.count(0) > 1:
            return(True)

        s = set(arr) - {0}

        for i in arr:
            if i * 2 in s:
                return(True)
        return(False)
