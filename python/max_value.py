# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii
from functools import cmp_to_key
from typing import List


class Solution:
    def compare(self, x, y):
        if x[1] == y[1]:
            return x[0] - y[0]
        return x[1] - y[1]

    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=cmp_to_key(self.compare))
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
