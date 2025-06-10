'''
242. Valid Anagram. https://leetcode.com/problems/valid-anagram/description/
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_map = {}

        if len(s) != len(t):
            return False

        for char in s:
            s_map[char] = s_map.get(char, 0) + 1
        
        for char in t:
            if char not in s_map:
                return False
            elif s_map[char] == 1:
                del s_map[char]
            else:
                s_map[char] -= 1
        
        if s_map:
            return False
        return True
