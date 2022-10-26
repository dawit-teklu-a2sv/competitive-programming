# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        int_list = []
        current = head
        while current:
            int_list.append(current.val)
            current = current.next
            
        output = [0] * len(int_list)
        stack = []
        for i,item in enumerate(int_list):
            while stack and int_list[stack[-1]] < item:
                output[stack.pop()] = item
            stack.append(i)
            
        return output
                
        