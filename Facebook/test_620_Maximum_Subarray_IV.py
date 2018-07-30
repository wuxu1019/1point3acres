"""
Description
Given an integer arrays, find a contiguous subarray which has the largest sum and length should be greater or equal to given length k.
Return the largest sum, return 0 if there are fewer than k elements in the array.

Ensure that the result is an integer type.

Have you met this question in a real interview?
Example
Given the array [-2,2,-3,4,-1,2,1,-5,3] and k = 5, the contiguous subarray [2,-3,4,-1,2,1] has the largest sum = 5.
"""


class Solution:
    """
    @param nums: an array of integer
    @param k: an integer
    @return: the largest sum
    """

    def maxSubarray4(self, nums, k):
        # write your code here
        if len(nums) < k:
            return 0
        sm = sum(nums[:k])
        base = sm
        max_g = sm
        max_l = sm
        for i in range(k, len(nums)):
            base = base + nums[i] - nums[i - k]
            max_l = max(max_l + nums[i], base)
            max_g = max(max_g, max_l)
        return max_g

