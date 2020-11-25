matrix = [
[1,2,3],
[4,5,6],
[7,8,9]]

def spiralOrder(matrix):

    result = []

    rowBegin = 0
    rowEnd = len(matrix) -1
    colBegin = 0
    colEnd = len(matrix[0]) - 1

    print(rowBegin, rowEnd, colBegin, colEnd)

    while rowBegin <= rowEnd and colBegin <= colEnd:
        for i in range(colBegin, colEnd+1):
            result.append(matrix[rowBegin][i])
        rowBegin += 1

        for i in range(rowBegin, rowEnd+1):
            result.append(matrix[i][colEnd])
        colEnd -= 1

        if rowBegin <= rowEnd:
            for i in range(colEnd, colBegin-1, -1):
                result.append(matrix[rowEnd][i])
            rowEnd -= 1

        if colBegin <= colEnd:
            for i in range(rowEnd, rowBegin-1, -1):
                result.append(matrix[i][colBegin])
            colBegin += 1

    return result

    # # starting row index
    # k = 0
    # # ending row index
    # m = w
    # # starting columns index
    # l = 0
    # # ending column index
    # n = h
    #
    # # if (k >= m or l >= n):
    # #     return
    #
    # # 1st row:
    # for i in range(k, n):
    #     result.append(matrix[k][i])
    #     # print(result)
    #
    # # last column
    # for i in range(k+1, m):
    #     result.append(matrix[i][n-1])
    #     # print(result)
    #
    # # last row if does not match with 1st
    # if (m - 1) != k:
    #     for i in range(n-2, l-1, -1):
    #         result.append(matrix[m-1][i])
    #
    # if (n - 1) != l:
    #     for i in range(m-2, i, -1):
    #         result.append(matrix[i][l])
    #
    # return result


print(spiralOrder(matrix))
