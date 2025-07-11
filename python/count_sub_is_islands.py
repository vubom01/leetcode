# https://leetcode.com/problems/count-sub-islands/description/

"""
- BFS
- Find the islands in grid2
- If any part of island is not part of an island in grid1, then that island is not a sub island
- Otherwise, increase the result by 1
- TC: O(n^2)
- SC: O(n^2)
"""

from typing import List


class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def isSubIslandsInGrid2(self, u: int, v: int, m: int, n: int,
                            grid1: List[List[int]], grid2: List[List[int]]) -> bool:

        isSubIslandsInGrid2 = (grid1[u][v] == 1)
        queue = [(u, v)]

        while len(queue) > 0:
            x, y = queue.pop(0)
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if grid2[nx][ny] == 1:
                        grid2[nx][ny] = 0
                        queue.append((nx, ny))
                        if grid1[nx][ny] == 0:
                            isSubIslandsInGrid2 = False

        return isSubIslandsInGrid2

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        result = 0

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    result += self.isSubIslandsInGrid2(i, j, m, n, grid1, grid2)
        return result


sol = Solution()
print(sol.countSubIslands(
    [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]],
    [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
))
