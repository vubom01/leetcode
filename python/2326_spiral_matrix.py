"""
https://leetcode.com/problems/spiral-matrix-iv/description/
"""

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1 for _ in range(n)] for _ in range(m)]
        p, total = 0, m * n
        while head:
            for i in range(p, n):
                if head is None: break
                res[p][i] = head.val
                head = head.next

            for i in range(p + 1, m):
                if head is None: break
                res[i][n - 1] = head.val
                head = head.next

            if p != m - 1:
                for i in range(n - 2, p - 1, -1):
                    if head is None: break
                    res[m - 1][i] = head.val
                    head = head.next

            if p != n - 1:
                for i in range(m - 2, p, -1):
                    if head is None: break
                    res[i][p] = head.val
                    head = head.next

            p += 1
            m -= 1
            n -= 1

        return res


sol = Solution()
print(sol.spiralMatrix(
    1,
    4,
    ListNode(
        val=1,
        next=ListNode(
            val=2,
            next=ListNode(
                val=0,
            )
        )
    ),
))
