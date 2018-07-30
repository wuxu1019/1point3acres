"""
Description
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Have you met this question in a real interview?
Example
For [4, 5, 1, 2, 3] and target=1, return 2.

For [4, 5, 1, 2, 3] and target=0, return -1.

Challenge
O(logN) time
"""


class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """

    def search(self, A, target):
        # write your code here
        l, r = 0, len(A) - 1

        while l <= r:
            m = (l + r) / 2
            if A[m] == target:
                return m
            elif (A[m] > A[l] and A[l] <= target < A[m]) or (A[m] < A[r] and not A[m] < target <= A[r]):
                r = m - 1
            else:
                l = m + 1

        return -1

if __name__ == '__main__':
    s = Solution()
    A = [0,1,2,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]
    target = -9

    rt = s.search(A, target)
    print rt