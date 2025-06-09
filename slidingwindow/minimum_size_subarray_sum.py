'''
209. Minimum Size Subarray Sum. https://leetcode.com/problems/minimum-size-subarray-sum/description/
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
'''


from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        result = float('inf')

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                result = min(r - l + 1, result)
                total -= nums[l]
                l += 1
        
        return 0 if result == float('inf') else result
