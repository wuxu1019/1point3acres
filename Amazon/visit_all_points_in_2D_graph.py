"""
give a n*n matrix, draw without break to connect all the points, also no repeat of any points

"""

def visite_all_points(matrix, si, sj):
    if not matrix:
        return False

    needtovisit = set()
    N = len(matrix)
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                needtovisit.add((i, j))

    visited = set()


    def dfs(i, j, visited, matrix, N):
        if i >= N or i < 0 or j >= N or j < 0 or matrix[i][j] == 0:
            if not visited - needtovisit and not needtovisit - visited:
                return True
            else:
                return False
        if (i, j) not in visited:
            moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for di, dj in moves:
                n_i = di + i
                n_j = dj + j
                visited.add((i, j))
                if dfs(n_i, n_j, visited, matrix, N):
                    return True
                visited.remove((i, j))
        return False

    return dfs(si, sj, visited, matrix, N)



if __name__ == '__main__':
    matrix = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    i, j = 0, 0
    rt = visite_all_points(matrix, i, j)
    print rt