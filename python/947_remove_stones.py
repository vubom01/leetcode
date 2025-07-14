"""
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/
"""

"""
- Use a disjoint set (union-find) data structure to identify the connected component
- TC: O(n)
- SC: O(n)
"""

from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = [-1 for _ in range(n)]

        def findSet(u: int) -> int:
            if parent[u] < 0:
                return u
            parent[u] = findSet(parent[u])
            return parent[u]

        def unionSet(u: int, v: int) -> int:
            u = findSet(u)
            v = findSet(v)
            if u == v:
                return 0
            if parent[u] > parent[v]:
                u, v = v, u
            parent[u] += parent[v]
            parent[v] = u
            return 1

        rows, cols = {}, {}
        result = 0
        for i in range(n):
            row = stones[i][0]
            col = stones[i][1]
            if row in rows:
                result += unionSet(i, rows[row])
            if row not in rows:
                rows[row] = i

            if col in cols:
                result += unionSet(i, cols[col])
            if col not in cols:
                cols[col] = i

        return result


sol = Solution()
print(sol.removeStones(
    [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
))
