# https://leetcode.com/problems/count-sub-islands/description/?envType=daily-question&envId=2024-08-28

from typing import List


class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def _isSubIslandsInGrid2(self, u: int, v: int, m: int, n: int, isVisit: List[List[bool]],
                             grid1: List[List[int]], grid2: List[List[int]]) -> bool:

        isSubIslandsInGrid2 = (grid1[u][v] == 1)
        queue = [(u, v)]
        isVisit[u][v] = True

        while len(queue) > 0:
            x, y = queue.pop(0)
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if isVisit[nx][ny] is False and grid2[nx][ny] == 1:
                        queue.append((nx, ny))
                        isVisit[nx][ny] = True
                        if grid1[nx][ny] == 0:
                            isSubIslandsInGrid2 = False

        return isSubIslandsInGrid2

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        result = 0

        isVisit = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and isVisit[i][j] is False:
                    result += self._isSubIslandsInGrid2(i, j, m, n, isVisit, grid1, grid2)
        return result


sol = Solution()
print(sol.countSubIslands(
    [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]],
    [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
))
