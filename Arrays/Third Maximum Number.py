nums = [2, 2, 3, 1]
nums2 = [1, 2]
nums3 = [1]
nums4 = [1, 1, 2]
nums5 = [1,2,2,5,3,5]

def thirdMax(nums):
    # Making sure that array is filled
    if nums == 0:
        return nums

    # If array has less than 3 elements return the max
    if len(nums) < 3:
        return max(nums)

    pos = []

    if len(nums) >= 3:
        # nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] not in pos:
                pos.append(nums[i])

        if len(pos) < 3:
            return max(pos)

        return pos[2]

print(thirdMax(nums5))

# Not correct output
def thirdMax(nums):
    s = set(nums)
    print(s)

    if len(s) < 3:
        return max(s)

    s.remove(max(s))
    s.remove(max(s))
    return(max(s))

print(thirdMax(nums5))
