class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        second = slow.next
        prev = slow.next = None


        while second:
            rem = second.next
            second.next = prev
            prev = second
            second = rem

        # print(head.next.val, left.next.val)
        # print(head, left)

        first, second = head, prev

        # print(left,right)

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first,second = temp1, temp2