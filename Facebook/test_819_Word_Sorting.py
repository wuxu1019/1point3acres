"""
Description
Give a new alphabet, such as {c,b,a,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z}. Sort the string array according to the new alphabet

The length of word does not exceed 100.
The number of words does not exceed 10000.
You can assume that the given new alphabet is a 26-character string.
Only lowercase letters.
Have you met this question in a real interview?
Example
Given Alphabet = {c,b,a,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z}, String array = {cab,cba,abc}, return {cba,cab,abc}.

Explanation:
According to the new dictionary order, output the sorted result {cba, cab, abc}.
Given Alphabet = {z,b,a,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,c}, String array = {bca,czb,za,zba,ade}, return {zba,za,bca,ade,czb}.

Explanation:
According to the new dictionary order, output the sorted result {zba,za,bca,ade,czb}.
"""


class Solution:
    """
    @param alphabet: the new alphabet
    @param words: the original string array
    @return: the string array after sorting
    """

    def wordSort(self, alphabet, words):
        # Write your code here
        mp = {}
        for i, v in enumerate(alphabet):
            mp[v] = i

        def compare_items(a, b):
            i = 0
            while i < min(len(a), len(b)):
                if mp[a[i]] > mp[b[i]]:
                    return 1
                elif mp[a[i]] < mp[b[i]]:
                    return -1
                i += 1
            if len(a) == len(b):
                return 0
            elif len(a) < len(b):
                return -1
            else:
                return 1

        return sorted(words, cmp=compare_items)