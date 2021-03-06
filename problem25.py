'''
25. Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def constructLinkedList(nodeList):
        head = ListNode(nodeList[0])
        l = head
        for i in nodeList[1:]:
            l.next = ListNode(i)
            l = l.next
        return head

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        l = []
        while head:
            l.append(head.val)
            head = head.next
        if len(l) == 0:
            return None

        for i in range(int(len(l)/k)):
            h = i*k
            t = (i+1)*k
            subl = l[h:t]
            subl.reverse()
            l = l[:h]+subl+l[t:]

        return constructLinkedList(l)


            





