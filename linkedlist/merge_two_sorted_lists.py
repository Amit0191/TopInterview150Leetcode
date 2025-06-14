'''
21. Merge Two Sorted Lists. https://leetcode.com/problems/merge-two-sorted-lists/description/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr =  dummy

        while list1 or list2:
            
            val1 = list1.val if list1 else float('inf')
            val2 = list2.val if list2 else float('inf')

            if val1 <= val2:
                curr.next = ListNode(val1)
                list1 = list1.next if list1 else None
            else:
                curr.next = ListNode(val2)
                list2 = list2.next if list2 else None
            
            curr = curr.next
        
        return dummy.next
