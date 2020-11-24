array = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ],
]

def findDiagonalOrder(array):
    result = {}
    counter = []

    for i in range(len(array)):
        for ii in range(len(array[i])):
            if i + ii not in result:
                result[i+ii] = [array[i][ii]]
                # print(result[i+ii],array[i][ii], i, ii)
            else:
                # print(result[i+ii], array[i][ii])
                result[i+ii].append(array[i][ii])

    for x in result.items():
        if x[0] % 2 == 0:
            [counter.append(x) for x in x[1][::-1]]
        else:
            [counter.append(x) for x in x[1]]

    return counter


print(findDiagonalOrder(array))
