"""
https://leetcode.com/problems/meeting-rooms-iii/description/
"""

"""
- Sort the meetings list in increasing order based on start time
- Use 2 to keep track of free rooms and active rooms in increasing order based on end time
- Loop through meeting
- Push all active rooms whose end time is earlier than the meeting's start time into the list of free rooms
- If there is a free room, assign it to the meeting 
- If not, assign the meeting to the active room that finishes first
- Update active rooms list
- Increment the counter for the room that was used
- TC: O(n log n)
- SC: O(n)
"""

import heapq
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        freeRooms = [i for i in range(n)]
        activeRooms = []
        counter = [0] * n

        for start, end in meetings:
            while len(activeRooms) and start >= activeRooms[0][0]:
                heapq.heappush(freeRooms, activeRooms[0][1])
                heapq.heappop(activeRooms)

            if len(freeRooms):
                room = heapq.heappop(freeRooms)
            else:
                t, room = heapq.heappop(activeRooms)
                end += t - start

            counter[room] += 1
            heapq.heappush(activeRooms, [end, room])

        return max(range(n), key=lambda x: (counter[x], -x))


s = Solution()
print(s.mostBooked(4, [[12, 44], [27, 37], [48, 49], [46, 49], [24, 44], [32, 38], [21, 49], [13, 30]]))
