from problem69 import Solution

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(4)

sol = Solution()

# print(sol.removeElement([2,2,3],2))
print(sol.mySqrt(4))

