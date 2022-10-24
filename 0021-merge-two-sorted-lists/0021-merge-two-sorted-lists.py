# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
         dummy = ListNode()
         tail = dummy
         while list1 and list2:
                if list1.val <= list2.val:
                    temp = ListNode(list1.val)
                    tail.next = temp
                    tail = temp
                    list1 = list1.next
                else:
                    temp = ListNode(list2.val)
                    tail.next = temp
                    tail = temp
                    list2 = list2.next     
         while list1:
            temp = ListNode(list1.val)
            tail.next = temp
            tail = temp
            list1 = list1.next
         while list2:
            temp = ListNode(list2.val)
            tail.next = temp
            tail = temp
            list2 = list2.next
            
         return dummy.next


            
            
            
        