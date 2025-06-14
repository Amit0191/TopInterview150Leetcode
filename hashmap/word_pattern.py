'''
290. Word Pattern. https://leetcode.com/problems/word-pattern/description/
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false
'''


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        pattern_to_word = {}
        word_to_pattern = {}

        s = s.split(' ')

        if len(s) != len(pattern):
            return False
        
        for i in range(len(s)):

            if (pattern[i] in pattern_to_word and pattern_to_word[pattern[i]] != s[i]) or  (s[i] in word_to_pattern and word_to_pattern[s[i]] != pattern[i]):
                return False
            
            pattern_to_word[pattern[i]] = s[i]
            word_to_pattern[s[i]] = pattern[i]
        
        return True
