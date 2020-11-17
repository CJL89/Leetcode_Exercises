nums = [1, 0, 0, 1, 1, 0, 1, 1, 1]
count = 0
ans = 0

for i in nums:
    # grabbing all matching 1s
    if i == 1:
        # if found a 1, increase count var by 1
        count += 1
        # get the max value
        ans = max(ans, count)
    else:
        count = 0
print(ans)
