"""
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
Follow up: Could you solve it in O(n2) runtime?
"""


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        nums.sort()
        ct = 0
        for i in range(len(nums) - 2):
            t = target - nums[i]

            l, r = i + 1, len(nums) - 1
            while l < r:
                while r > l and nums[l] + nums[r] >= t:
                    r -= 1
                while r > l and nums[l] + nums[r] < t:
                    ct += r - l
                    l += 1

        return ct