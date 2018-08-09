"""
Given a grid where each entry is only 0 or 1, find the number of corner rectangles.

A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle. Note that only the corners need to have the value 1. Also, all four 1s used must be distinct.



Example 1:

Input: grid =
[[1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 0, 0, 1, 0],
 [1, 0, 1, 0, 1]]
Output: 1
Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].


Example 2:

Input: grid =
[[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]]
Output: 9
Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.


Example 3:

Input: grid =
[[1, 1, 1, 1]]
Output: 0
Explanation: Rectangles must have four distinct corners.
"""

class Solution(object):
    def countCornerRectangles_bruteforce(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        R, C = len(grid), len(grid[0])
        rt = 0
        for i in range(R - 1):
            for k in range(i + 1, R):
                count = 0
                for j in range(C):
                    if grid[i][j] and grid[k][j]:
                        rt += count
                        count += 1
        return rt
    def countCornerRectangles_dp(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        R, C = len(grid), len(grid[0])
        dp = []
        rt = 0
        for i in range(R):
            dp.append(set(j for j in range(C) if grid[i][j]))
            for k in range(i):
                match = len(dp[k] & dp[i])
                rt += match * (match - 1) / 2
        return rt