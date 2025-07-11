"""
https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/description/
"""

"""
- With k events, we can shift all the events to the left so that the distance to the (k+1)th event is maximized
- When adding a new event to the k-segment, remove the event at the start of the segment
- Recalculate the end time
- TC: O(n)
- SC: O(1)
"""

from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        res = 0
        sum = 0
        startTime.append(eventTime)
        for i in range(n):
            sum += endTime[i] - startTime[i]
            if i < k:
                end = sum
            else:
                end = sum + startTime[i - k]
                sum -= endTime[i - k] - startTime[i - k]
            res = max(res, startTime[i + 1] - end)
        return res


s = Solution()
print(s.maxFreeTime(59, 2, [5, 9, 22, 24, 40], [7, 15, 23, 27, 42]))
