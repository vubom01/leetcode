# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/?envType=daily-question&envId=2024-09-10

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
        node = head
        while node is not None:
            if node.next is not None:
                a = node.val
                b = node.next.val
                newNode = ListNode(
                    val = self.findGreatestCommonDivisior(a, b),
                    next = node.next
                )
                node.next = newNode
                node = node.next

            node = node.next

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
