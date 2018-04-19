"""
Find the minimum distance between two numbers
Given an unsorted array arr[] and two numbers x and y, find the minimum distance between x and y in arr[]. The array might also contain duplicates. You may assume that both x and y are different and present in arr[].

Examples:
Input: arr[] = {1, 2}, x = 1, y = 2
Output: Minimum distance between 1 and 2 is 1.

Input: arr[] = {3, 4, 5}, x = 3, y = 5
Output: Minimum distance between 3 and 5 is 2.

Input: arr[] = {3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3}, x = 3, y = 6
Output: Minimum distance between 3 and 6 is 4.

Input: arr[] = {2, 5, 3, 5, 4, 4, 2, 3}, x = 3, y = 2
Output: Minimum distance between 3 and 2 is 1.
"""

def minDist(l, a, b):
    """find the min distance between a b in l"""
    pre = 0
    rt = float('INF')
    for i in range(len(l)):
        if l[i] == a or l[i] == b:
            pre = i
            break

    for i in range(pre+1, len(l)):
        if l[i] == a or l[i] == b:
            if l[i] != l[pre] and i - pre < rt:
                rt = i - pre
            pre = i
    return rt

if __name__ == '__main__':
    l = [3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
    a = 3
    b = 6
    rt1 = minDist(l, a, b)
    print rt1