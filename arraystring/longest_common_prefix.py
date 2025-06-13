'''
14. Longest Common Prefix. https://leetcode.com/problems/longest-common-prefix/description/
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''


from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_len = min(len(s) for s in strs)
        lcp = 0
        for i in range(min_len):
            for s in strs:
                if strs[0][i] != s[i]:
                    break
            else:
                lcp += 1
                continue
            break
    
        return '' if lcp == 0 else strs[0][0: lcp]
