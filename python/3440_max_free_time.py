"""
https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/description/
"""

"""
- For the i-th event, check if it can be moved before event i-1 or after event i+1
- The free time is calculated based on event i-1 and event i+1
- If not, move event i to the end time of event i-1, and update the free time based on event i+1
- TC: O(n)
- SC: O(n)
"""

from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)

        startTime.append(eventTime)
        endTime.append(0)

        maxR = [0] * n
        for i in range(n - 2, -1, -1):
            maxR[i] = max(maxR[i + 1], startTime[i + 2] - endTime[i + 1])

        res = 0
        maxL = 0
        for i in range(n):
            res = max(res, startTime[i + 1] - (endTime[i - 1] + endTime[i] - startTime[i]))
            if max(maxL, maxR[i]) >= endTime[i] - startTime[i]:
                res = max(res, startTime[i + 1] - endTime[i - 1])
            maxL = max(maxL, startTime[i] - endTime[i - 1])

        return res


s = Solution()
print(s.maxFreeTime(37, [5, 14, 27, 34], [13, 18, 31, 37]))
