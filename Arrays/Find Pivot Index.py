nums = [1,7,3,6,5,6]
nums2 = [-1,-1,-1,-1,-1,0]
nums3 = []

def pivotIndex(nums):
    if len(nums) == 0:
        return -1

    total = sum(nums)
    count = 0

    for i in range(len(nums)):
        if nums[i] == total - 2 * count:
            return i
        else:
            count += nums[i]

    return -1

print(pivotIndex(nums3))
