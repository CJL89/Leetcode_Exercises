heights = [1,1,4,2,1,3]

def heightChecker(heights):
    if len(heights) == 0:
        return heights

    sorted_heights = [x for x in sorted(heights)]

    count = 0

    for i in range(len(heights)):
        if heights[i] != sorted_heights[i]:
            count += 1

    return count

print(heightChecker(heights))
