# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Space complexity: O(1) - no added space
        # Time complexity: O(N) - have to go through each node and change its next
        prev, curr = None, head
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev