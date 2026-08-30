class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = ""
        b = ""

        while l1 != None:
            a = a + str(l1.val)
            l1 = l1.next

        while l2 != None:
            b = b + str(l2.val)
            l2 = l2.next

        a = a[::-1]
        b = b[::-1]

        res = int(a) + int(b)

        l3 = None

        if res == 0:
            return ListNode(0)

        l3 = None
        tail = None

        while res > 0:
            i = res % 10
            new_node = ListNode(i)

            if l3 == None:
                l3 = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node

            res = res // 10

        return l3
