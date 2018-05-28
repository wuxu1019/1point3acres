"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.


"""

class Solution(object):
    def islandPerimeter(self, grid):
        if not grid:
            return 0
        R, C = len(grid), len(grid[0])
        self.visited = set()
        count = 0
        for i in range(R):
            for j in range(C):
                if (i, j) not in self.visited and grid[i][j]:
                    count += self.islandPerimeterHelper(grid, i , j, R, C)
        return count

    def islandPerimeterHelper(self, grid, i, j, R, C):
        self.visited.add((i, j))
        move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ct = 0
        for di, dj in move:
            new_i = i + di
            new_j = j + dj
            if new_i >= R or new_i < 0 or new_j >= C or new_j < 0:
                ct += 1
                continue
            if grid[new_i][new_j]:
                if (new_i, new_j) not in self.visited:
                    ct += self.islandPerimeterHelper(grid, new_i, new_j, R, C)
            else:
                ct += 1
        return ct

if __name__ == '__main__':
    s = Solution()
    grid = [[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
    rt = s.islandPerimeter(grid)
    print rt