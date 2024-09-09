# https://leetcode.com/problems/spiral-matrix-iv/description/?envType=daily-question&envId=2024-09-09

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1 for _ in range(n)] for _ in range(m)]
        cnt, p, total = 0, 0, m * n
        while cnt < total:
            for i in range(p, n):
                res[p][i] = head.val if head is not None else - 1
                head = head.next if head is not None else None

            for i in range(p + 1, m):
                res[i][n - 1] = head.val if head is not None else - 1
                head = head.next if head is not None else None

            if p != m - 1:
                for i in range(n - 2, p - 1, -1):
                    res[m - 1][i] = head.val if head is not None else - 1
                    head = head.next if head is not None else None

            if p != n - 1:
                for i in range(m - 2, p, -1):
                    res[i][p] = head.val if head is not None else - 1
                    head = head.next if head is not None else None

            if head is None:
                break

            p += 1
            m -= 1
            n -= 1

        return res

sol = Solution()
print(sol.spiralMatrix(
    1,
    4,
    ListNode(
        val = 1,
        next = ListNode(
            val = 2,
            next=ListNode(
                val = 0,
            )
        )
    ),
))
