'''
383. Ransom Note. https://leetcode.com/problems/ransom-note/description/
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
'''


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(magazine) < len(ransomNote):
            return False
        
        magazine_dict = {}
        for i in magazine:
            magazine_dict[i] = magazine_dict.get(i, 0) + 1
        
        for i in ransomNote:
            if i not in magazine_dict:
                return False
            elif magazine_dict[i] == 1:
                del magazine_dict[i]
            else:
                magazine_dict[i] -= 1

        return True