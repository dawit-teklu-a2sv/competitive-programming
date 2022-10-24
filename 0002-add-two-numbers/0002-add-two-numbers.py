# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        l3 = dummy_head
        carray = 0
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            val = n1 + n2 + carray
            last_digit = val % 10
            carray = val // 10 
            new_node = ListNode(last_digit)
            l3.next = new_node
            l3 = l3.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        if(carray):
            new_node =ListNode(carray)
            l3.next = new_node
            l3 = l3.next
        return dummy_head.next