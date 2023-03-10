# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow,fast = head,head.next
        while fast and fast.next:
            fast= fast.next.next
            slow = slow.next
        
        mid = slow.next
        slow.next = None
        
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.mergeTwoLists(left,right)
        
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next
#         if not list1:
#             return list2
#         if not list2:
#             return list1
        
#         if list1.val < list2.val:
#             list1.next = self.mergeTwoLists(list1.next,list2)
#             return list1
             
#         list2.next = self.mergeTwoLists(list1,list2.next)
#         return list2
        
#         return self.mergeTwoLists(list1,list2)