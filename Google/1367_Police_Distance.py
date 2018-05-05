"""
Given a matrix size of n x m, element 1 represents policeman, -1 represents wall and 0 represents empty.
Now please output a matrix size of n x m, output the minimum distance between each empty space and the nearest policeman

 Notice
Given a matrix size of n x m， n <= 200，m <= 200.
We guarantee that each empty space can be reached by one policeman at least.
Have you met this question in a real interview?
Example
Given mat =

[
    [0, -1, 0],
    [0, 1, 1],
    [0, 0, 0]
]
return [[2,-1,1],[1,0,0],[2,1,1]].

The distance between the policeman and himself is 0, the shortest distance between the two policemen to other empty space is as shown above
Given mat =

[
    [0, -1, -1],
    [0, -1, 1],
    [0, 0, 0]
]
````
return `[[5,-1,-1],[4,-1,0],[3,2,1]]`。
The shortest distance between the policemen to other 5 empty space is as shown above.
"""


def getDistance(matrix):
    R, C = len(matrix), len(matrix[0])
    ML = R + C

    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
            elif matrix[i][j] != -1
                up = matrix[i-1][j] if i > 0 and matrix[i-1][j] != -1 else ML
                left = matrix[i][j-1] if j > 0 and matrix[i][j-1] != -1 else ML
                matrix[i][j] = min(up, left) + 1

    for i in range(R-1, -1, -1):
        for j in range(C-1, -1, -1):
            if matrix[i][j] != -1:
                down = matrix[i + 1][j] if i + 1 < R and matrix[i + 1][j] != -1 else ML
                right = matrix[i][j + 1] if j + 1 < C and matrix[i][j + 1] != -1 else ML
                matrix[i][j] = min(min(down, right)+1, matrix[i][j])

    return matrix


matrix = [[0, -1, 0],[0, 1, 1],[0, 0, 0]]
rt = getDistance(matrix)
print rt
