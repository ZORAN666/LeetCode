# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 特殊情况
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        # 如果 相加 小于 10 ，不需要进位
        if l1.val + l2.val < 10:
            l3 = ListNode(l1.val + l2.val)
            l3.next = self.addTwoNumbers(l1.next, l2.next)
        # 相加大于等于 10，需要进位
        elif l1.val + l2.val >= 10:
            l3 = ListNode(l1.val + l2.val - 10)
            tmp = ListNode(1)
            tmp.next = None
            # 递归调用
            l3.next = self.addTwoNumbers(l1.next, self.addTwoNumbers(l2.next ,tmp))
        return l3
    
la = ListNode(2)
la.next = ListNode(4)
la.next.next = ListNode(3)

lb = ListNode(5)
lb.next = ListNode(6)
lb.next.next = ListNode(4)

s = Solution()
ss = s.addTwoNumbers(la, lb)
print(ss.val)
print(ss.next.val)
print(ss.next.next.val)
