class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# two pointers
        left, right = None, head

        while right:
            rem = right.next
            right.next = left
            left = right
            right = rem

        return left