"""
https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/description/
"""

"""
- DP bitmask
- Use bitmask to describe the state of the players. If the i-th bit is 1, it means player-i is winner
- For each pair (i, n-i-1), choose a winner, always picking firstPlayer and secondPlayer
- dp_min[bitmask] = min(dp_min[next_bitmask] + 1)
- dp_max[bitmask] = max(dp_max[next_bitmask] + 1)
- If firstPlayer meets secondPlayer, then both dp_min[bitmask] and dp_max[bitmask] are equal 1
- Optimize
  -- dp_min[n][f][s] = min(dp_min[m][next_f][next_s] + 1)
  -- dp_max[n][f][s] = max(dp_max[m][next_f][next_s] + 1)
  -- n is the length of the list of players
  -- m is the length of the list of winners
  -- next_f is the new index of f in the list of winners
  -- next_s is the new index of s in the list of winners
  -- If f + s == n - 1, dp[n][f][s] = 1
- Cache the result of each bitmask to optimize runtime
- Use backtrack and memcache
- TC: O(n * state)
- SC: O(state)  
"""

from functools import lru_cache
from typing import List


class Solution:
    @lru_cache(None)
    def dp(self, n, f, s):
        if f + s == n - 1:
            return 1, 1

        nextMasks = [1 << (n // 2) if n & 1 else 0]
        for i in range(n // 2):
            p1, p2 = i, n - i - 1
            newMasks = []
            for mask in nextMasks:
                if p1 in (f, s):
                    newMasks.append(mask | (1 << p1))
                elif p2 in (f, s):
                    newMasks.append(mask | (1 << p2))
                else:
                    newMasks.append(mask | (1 << p1))
                    newMasks.append(mask | (1 << p2))
            nextMasks = newMasks

        minRes = float('inf')
        maxRes = 0

        for mask in nextMasks:
            winners = []
            for i in range(n):
                if (mask >> i) & 1:
                    winners.append(i)

            minR, maxR = self.dp(len(winners), winners.index(f), winners.index(s))
            minRes = min(minRes, minR + 1)
            maxRes = max(maxRes, maxR + 1)

        return minRes, maxRes

    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        if firstPlayer > secondPlayer:
            firstPlayer, secondPlayer = secondPlayer, firstPlayer
        return list(self.dp(n, firstPlayer - 1, secondPlayer - 1))


s = Solution()
print(s.earliestAndLatest(25, 18, 20))
