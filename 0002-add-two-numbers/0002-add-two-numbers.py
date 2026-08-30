
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Store the digits from both linked lists as strings.
        # The lists store digits in reverse order, so we will reverse
        # these strings later to obtain the actual numbers.
        a = ""
        b = ""

        # Traverse l1 and collect each node's digit in order.
        while l1 != None:
            a = a + str(l1.val)
            l1 = l1.next

        # Traverse l2 and collect each node's digit in order.
        while l2 != None:
            b = b + str(l2.val)
            l2 = l2.next

        # Reverse the strings because the linked lists store the
        # least significant digit first.
        # Example: [2,4,3] represents 342, not 243.
        a = a[::-1]
        b = b[::-1]

        # Convert the strings to integers and calculate the sum.
        res = int(a) + int(b)

        # 'l3' will point to the first node (head) of the result list.
        # 'tail' will point to the last node so that new nodes can
        # be appended efficiently.
        l3 = None
        tail = None

        # If the sum is zero, return a single node containing 0.
        if res == 0:
            return ListNode(0)

        # Extract digits from right to left and use them to build
        # the result linked list in the required reverse order.
        while res > 0:

            # % 10 gives the rightmost digit of the number.
            i = res % 10

            # Create a new node containing the extracted digit.
            new_node = ListNode(i)

            # For the first digit, initialize both the head and tail.
            if l3 == None:
                l3 = new_node
                tail = new_node

            # For subsequent digits, append the new node after the tail
            # and move the tail pointer to the newly added node.
            else:
                tail.next = new_node
                tail = new_node

            # // 10 removes the rightmost digit from the number.
            res = res // 10

        # Return the head of the newly created result linked list.
        return l3
