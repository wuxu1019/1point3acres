"""
count island, the given matrix, each line is different
"""

def count_island(matrix):

    if not matrix:
        return 0

    ct = 0

    for i, line in enumerate(matrix):
        for j, v in enumerate(line):
            if v == 1:
                ct += 1
                dfs(i, j, matrix)
    return ct

def dfs(i, j, matrix):
    matrix[i][j] = 0

    moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    for di, dj in moves:
        n_i, n_j = i + di, j + dj
        if 0 <= n_i < len(matrix) and 0 <= n_j < len(matrix[n_i]) and matrix[n_i][n_j] == 1:
            dfs(n_i, n_j, matrix)

if __name__ == "__main__":
    matrix = [[1], [1, 1, 1, 1, 1], [0, 1, 0]]
    rt = count_island(matrix)
    print rt

