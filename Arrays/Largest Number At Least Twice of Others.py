nums1 = [3, 6, 1, 0]
nums2 = [1, 2, 3, 4]
nums = [0,0,0,1]
nums3 = [1]
nums4 = [1,0]
nums5 = [0,0,1,2]
nums6 = [0,1]
nums7 = [0,0,1,0]
nums8 = [0,0,1,3]
nums9 = [0,0,2,3]

def dominantIndex(nums):
    if nums == 0:
        return nums

    highest = -1
    second = -1
    idx = 0

    for i, n in enumerate(nums):
        if n >= highest:
            second = highest
            highest = n
            idx = i
            print(highest, second, idx, n)
        elif n > second:
            second = n

    if highest < second * 2:
        idx = -1

    return idx


print(dominantIndex(nums9))
