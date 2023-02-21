# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow=fast=head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        current = slow
        
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True