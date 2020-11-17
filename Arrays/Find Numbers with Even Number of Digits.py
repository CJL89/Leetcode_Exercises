nums = [555,901,482,1771,12,1234,1,2,4,5,6,120405]
count = 0

for i in nums:
    digits = len(str(i)) % 2
    if digits == 0:
        count += 1
print(count)
