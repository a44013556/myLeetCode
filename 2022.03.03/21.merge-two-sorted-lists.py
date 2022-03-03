#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = now = ListNode(0)

        while list1 and list2:
            if list1.val > list2.val:
                now.next = ListNode(list2.val)
                list2 = list2.next
            else:
                now.next = ListNode(list1.val)
                list1 = list1.next
            now = now.next
        if list1:now.next = list1
        if list2:now.next = list2
        return res.next
# @lc code=end

