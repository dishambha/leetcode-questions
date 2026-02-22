# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        a = head
        b = head.next
        while b != None:
            while b != None and b.val == a.val:
                b = b.next
            a.next = b
            a = b
            if b != None:
                b = b.next
        return head
        