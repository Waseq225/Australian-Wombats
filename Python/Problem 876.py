# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        count = 0
        length = 0
        while temp:
            length += 1
            temp = temp.next

        if length == 1:
            return head

        mid = int(length / 2)
        count = 0
        while head:
            count += 1
            head = head.next
            if count == mid:
                return head
