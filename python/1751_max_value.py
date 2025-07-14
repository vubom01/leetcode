"""
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/description/
"""

""" 
- Dynamic Programming
- Sort the events list in increasing order based on end time
- dp[i][j] is the highest score achievable by attending j events among the events from 0 to i
- If we do not attend event j -> dp[i][j] = dp[i-1][j]
- Otherwise, dp[i][j] = max(dp[t][j-1] + val[i]) for t in [0, i-1] such that start[i] >= end[t]
- Because dp[i][j] depends on dp[i-1][j], we only need to find the largest t
- dp[i][j] = max(dp[i-1][j], dp[t][j-1] + val[i])
- Use binary search to find t
- TC: O(n log n)
- SC: O(n * k)
"""

from typing import List


class Solution:
    def compare(self, x, y):
        if x[1] == y[1]:
            return x[0] - y[0]
        return x[1] - y[1]

    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        res = 0

        for i in range(1, n + 1):
            start, end, val = events[i - 1]

            prevEvent = 0
            left, right = 0, i - 2
            while left <= right:
                mid = (left + right) // 2
                if events[mid][1] < start:
                    prevEvent = mid + 1
                    left = mid + 1
                else:
                    right = mid - 1

            dp[i][1] = val
            for j in range(1, k + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[prevEvent][j - 1] + val)
                res = max(res, dp[i][j])

        return res


s = Solution()
print(s.maxValue([[1, 2, 4], [3, 4, 3], [2, 3, 10]], 2))
