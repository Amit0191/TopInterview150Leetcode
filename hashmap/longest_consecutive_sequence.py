'''
128. Longest Consecutive Sequence. https://leetcode.com/problems/longest-consecutive-sequence/description
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
'''


from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numbers = set(nums)
        res = 0
        for num in numbers:
            
            if num - 1 not in numbers:
                length = 1
                while num + length in numbers:
                    length += 1

                res = max(res, length)
        return res