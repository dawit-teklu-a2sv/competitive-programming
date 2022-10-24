# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        output = []
        while head:
            output.append(head.val)
            head = head.next
        if not output:
            return head
        head = ListNode(output[-1])
        print(output)
        dummy = ListNode(0,head)
        for i in range(len(output) - 2, -1,-1):
            node = ListNode(output[i])
            head.next = node
            head = node 
            
        return dummy.next
            