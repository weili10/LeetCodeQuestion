from problem88 import Solution

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(1)
l2.next.next = ListNode(2)
l2.next.next.next = ListNode(3)
l2.next.next.next.next = ListNode(3)
sol = Solution()


print(sol.merge([1,3,5,7,9],5,[2,4,6,8],4))

# l = sol.deleteDuplicates(l2)
# while l:
#     print(l.val)
#     l = l.next

