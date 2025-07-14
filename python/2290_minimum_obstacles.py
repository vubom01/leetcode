"""
https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/description/
"""

"""
- distance[u][v] is the minimum number of obstacles that need to remove to go from (0, 0) to (u,v)
- Solution 1: Use Dijkstra's algorithm to find the shortest path on a weighted graph
  -- TC: O(n * m * log(n * m))
  -- SC: O(n * m)
- Solution 2: Use BFS
  -- TC: O(n * m)
  -- SC: O(n * m)
"""

import heapq
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        distance = [[100005 for _ in range(m)] for _ in range(n)]
        distance[0][0] = 0
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        # Dijkstra
        heap = [(0, 0, 0)]
        while heap:
            d, i, j = heapq.heappop(heap)
            if distance[i][j] != d:
                continue
            if i == n - 1 and j == m - 1:
                return d
            for k in range(4):
                u = i + dx[k]
                v = j + dy[k]
                if 0 <= u < n and 0 <= v < m:
                    if distance[u][v] > d + (grid[u][v] == 1):
                        distance[u][v] = d + (grid[u][v] == 1)
                        heapq.heappush(heap, (distance[u][v], u, v))

        # BFS
        in_queue = [[False for _ in range(m)] for _ in range(n)]
        queue = [(0, 0)]
        in_queue[0][0] = True
        while queue:
            i, j = queue.pop(0)
            in_queue[i][j] = False
            for k in range(4):
                u = i + dx[k]
                v = j + dy[k]
                if 0 <= u < n and 0 <= v < m:
                    if distance[u][v] > distance[i][j] + (grid[u][v] == 1):
                        distance[u][v] = distance[i][j] + (grid[u][v] == 1)
                        if in_queue[u][v] is False:
                            queue.append((u, v))
                            in_queue[u][v] = True
        return distance[n - 1][m - 1]
