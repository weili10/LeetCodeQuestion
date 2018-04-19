from problem31 import Solution

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def constructLinkedList(nodeList):
    head = ListNode(nodeList[0])
    l = head
    for i in nodeList[1:]:
        l.next = ListNode(i)
        l = l.next
    return head


# sol = Solution()

# # nl = [5,62,17,20,2,30,58,40,94,78,31,62,21,92,30,61,10,54,88,63,35,89,24,33,48,31,35,46,35,6,87,40,68,57,60,22,87,70,63,33,0,94,95,22,38,77,35,48,31,24,63,19,65,88,4,14,71,39,60,6,45,48,99,65,57,11,88,44,82,51,77,82,97,25,56,35,2,92,36,86,68,99,5,33,39,9,99,11,0,60,69,97,60,68,62,17,32,50,13,14,1,42,48,98,67,5,86,22,97,74,8,65,25,65,50,65,26,50,28,26,10,97,23,22,18,85,91,2,88,56,16,41,98,64,92,18,21,78,92,18,4,0,83,29,17,34,94,43,36,74,69,98,24,44,20,94,29,63,96,69,19,12,11,69,28,3,87,50,33,31,20,37,31,56,18,48,42,13,43,78,39,12,76,63,56,48,57,38,11]
# # nl = [1,2,3,4,5,6,7]
# l1 = constructLinkedList(nl)
# l = sol.reverseKGroup(l1,12)
# while l:
#     print(l.val)
#     l = l.next


sol = Solution()
print(sol.nextPermutation([1,3,2]))
