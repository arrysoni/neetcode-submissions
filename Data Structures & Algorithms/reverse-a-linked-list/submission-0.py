# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev_node = None
        curr_node = head

        while curr_node:

            # 1. save next node
            next_node = curr_node.next

            # 2. reverse pointer
            curr_node.next = prev_node

            # 3. move prev
            prev_node = curr_node
            # 4. move curr
            curr_node = next_node

        return prev_node

            
        