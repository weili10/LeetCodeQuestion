'''
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        nl = head
        
        while l1 and l2:
            if l1.val <= l2.val:
                nl.next = l1
                l1 = l1.next
            else:
                nl.next = l2
                l2 = l2.next
            nl = nl.next
            
        if l1:
            nl.next = l1
        if l2:
            nl.next = l2

        return head

