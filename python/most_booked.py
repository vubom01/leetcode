# https://leetcode.com/problems/meeting-rooms-iii
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
