# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=fast=head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        previous = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = previous
            previous = curr
            curr = temp
        output = -float('inf')
        while head and previous:
            output = max(head.val + previous.val,output)
            head = head.next
            previous = previous.next
        return output
        