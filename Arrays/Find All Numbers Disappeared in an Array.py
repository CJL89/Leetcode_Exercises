nums1 = [4,3,2,7,8,2,3,1]
nums = [1,1]

def findDisappearedNumbers(nums):
    if len(nums) == 0:
        return nums

    count = []
    set_nums = set(nums)
    print(set_nums)

    # for i in range(1,len(set_nums)+1):
        # return [i not in set_nums]
    return [i for i in range(1, len(nums)+1) if i not in set_nums]

print(findDisappearedNumbers(nums))
