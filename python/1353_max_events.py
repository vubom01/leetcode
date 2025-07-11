"""
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description/
"""

"""
- Greedy
- Sort the events list
- For each day, find the event that can be attended
- If there are multiple events, select the event with the minimum end time
- TC: O(maxDay log n)
- SC: O(n)
"""

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
