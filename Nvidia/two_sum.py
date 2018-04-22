# coding=utf-8
"""
two sum, output all possibility
"""
import collections

def twoSum(nums, target):
     rt = []
     record = collections.defaultdict(int)
     for num in nums:
         diff = target - num
         if diff in record:
             for _ in range(record[diff]):
                 rt.append((diff, num))
         record[num] += 1
     return rt

if __name__ == '__main__':
    l = [2, 2, 4, 2, 6, 4, 6, 7, 2, 3, 4, 5, 7, 8, 1]
    target = 10

    rt = twoSum(l, target)
    print rt