arr = [1,0,2,3,0,4,5,0]
y = [1,2,3]

arr2 = [i for i in arr]
print(arr2)
i = 0
j = 0

while i < len(arr):
    if not arr2[j]:
        print(arr2)
#         arr[i] = 0
#         i += 1
#         if  i < len(arr):
#             arr[i] = 0
#     else:
#         arr[i] = arr2[j]
#     j += 1
#     i += 1
# print(arr)

# for i in range(len(arr)-1, -1, -1):
#     if i + zeros < len(arr):
#         print(i, zeros, len(arr))
