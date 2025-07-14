"""
https://leetcode.com/problems/maximum-matching-of-players-with-trainers/description/
"""

"""
- Greedy
- Sort the players list
- Sort the trainers list
- For each player, find the trainer with the minimum capacity that can still match the player
- TC: O(n log n)
- SC: O(1)
"""

from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i, j = 0, 0
        res = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                res += 1
                i += 1
            j += 1

        return res


s = Solution()
print(s.matchPlayersAndTrainers([4, 7, 9], [8, 2, 5, 8]))
