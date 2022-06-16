# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        
        node = head
        
        while(node):
            lst.append(node.val)
            node = node.next
            
        node = head
        for i in reversed(range(len(lst))):
            node.val = lst[i]
            node = node.next
            
        return head
        