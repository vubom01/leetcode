"""
https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def findGreatestCommonDivisior(self, a: int, b: int) -> int:
        if b == 0:
            return a
        return self.findGreatestCommonDivisior(b, a % b)

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            gcd = self.findGreatestCommonDivisior(current.val, current.next.val)
            current.next = ListNode(gcd, current.next)
            current = current.next.next
        return head


sol = Solution()
print(sol.insertGreatestCommonDivisors(
    ListNode(
        val=18,
        next=ListNode(
            val=6,
            next=ListNode(
                val=10,
                next=ListNode(
                    val=3,
                )
            )
        )
    ),
))
