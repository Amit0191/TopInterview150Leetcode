"""
Link: https://leetcode.com/problems/merge-sorted-array/description/
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 
Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

         
        l = m - 1
        r = n - 1
        l_plus_r = m + n - 1
        

        while l >= 0 and r >= 0:
            if nums1[l] >= nums2[r]:
                nums1[l_plus_r] = nums1[l]
                l -= 1
            else:
                nums1[l_plus_r] = nums2[r]
                r -= 1
            l_plus_r -= 1

        if l < 0:
            for i in range(r+1):
                nums1[i] = nums2[i]
        return