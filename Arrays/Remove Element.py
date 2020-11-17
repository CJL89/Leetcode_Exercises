nums = [3,2,2,3]
val = 2

# nums = [x for x in nums if x != val]
# print(nums)

while val in nums:
    nums.remove(val)

print(nums)
