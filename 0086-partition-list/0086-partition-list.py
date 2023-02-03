# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        left = ListNode(0)
        right = ListNode(0)
        
        leftTail = left
        rightTail = right
        
        temp = head
        while temp:
            if temp.val < x:
                leftTail.next = temp
                leftTail = leftTail.next
            else:
                rightTail.next = temp
                rightTail = rightTail = rightTail.next
        
            temp = temp.next
        leftTail.next = right.next
        rightTail.next = None
        return left.next
        
