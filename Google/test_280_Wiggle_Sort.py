"""
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
"""


class Solution(object):
    def wiggleSort_nlog(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        if len(nums) % 2 == 0:
            nums[0:len(nums):2], nums[1:len(nums):2] = nums[0:len(nums) / 2], nums[len(nums) / 2:]
        else:
            nums[0:len(nums):2], nums[1:len(nums):2] = nums[0:len(nums) / 2 + 1], nums[len(nums) / 2 + 1:]

    def wiggleSort_On(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            if i % 2 == 1 and nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            elif i % 2 == 0 and nums[i - 1] < nums[i]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]

