nums = [1,1,2,2]
nums2 = [0,0,1,1,1,2,2,3,3,4]


def removeDuplicates(nums):
    # Return in case array is empty
    if len(nums) == 0:
        return nums

    # Creating counter
    count = []

    # Loop though array:
    for i in range(len(nums)):
        print(i)
        if nums[i] != nums[i-1]:
            count.append(nums[i])
    return count

print(removeDuplicates(nums2))

# 2nd solution:
# 
# def removeDuplicates(nums):
#     if len(nums) == 0:
#         return nums
#
#     count = 0
#
#     for i in range(1, len(nums)):
#         if nums[i] != nums[i-1]:
#             count += 1
#             nums[count] = nums[i]
#
#     return count + 1
#
# print(removeDuplicates(nums2))
