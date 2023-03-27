# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        temp = head
        while temp:
            size += 1
            temp = temp.next
        if not head or size == 1:
            return head
        k = k % size
        if k == 0:
            return head
        fast =slow= head
        
        while fast and k > 0:
            fast = fast.next
            k -= 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        temp = slow.next
        slow.next = None
        fast.next = head
        head = temp
        return head
#         dummy = ListNode(0,temp)
#         while temp and k > 0:
#             temp = temp.next
#             k -= 1
#         while temp and temp.next:
#             slow = slow.next
#             temp = temp.next.next
        
        
#         new_head = slow.next
#         print(new_head)
#         slow.next = None
#         temp = new_head
#         print(temp)
#         while temp and temp.next:
#             temp = temp.next 
#         print(temp)
#         temp.next = dummy.next
#         return new_head
        
