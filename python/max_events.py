# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended
import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        maxDay = events[-1][1]
        res = 0
        openEvents = []
        idx = 0
        for d in range(1, maxDay + 1):
            while len(openEvents) and openEvents[0] < d:
                heapq.heappop(openEvents)
            while idx < len(events) and events[idx][0] <= d:
                heapq.heappush(openEvents, events[idx][1])
                idx += 1
            if len(openEvents):
                heapq.heappop(openEvents)
                res += 1
        return res


s = Solution()
print(s.maxEvents([[1, 2], [1, 2], [1, 6], [1, 2], [1, 2]]))
