# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/

"""
- We can calculate the total skill of each team: sumOfEachTeam
- Sort the skill list
- Always pair the strongest player with the weakest player
- If the total skill of the two players is not equal to sumOfEachTeam, return -1
- TC: O(n log n)
- SC: O(1)
"""

from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        sumOfEachTeam = int(sum(skill) / (len(skill) / 2))

        result = 0
        l, r = 0, len(skill) - 1
        while l < r:
            if skill[l] + skill[r] != sumOfEachTeam:
                return -1
            result += skill[l] * skill[r]
            l += 1
            r -= 1

        return result


sol = Solution()
print(sol.dividePlayers([3, 2, 5, 1, 3, 4]))

# def test():
#     inputs = [[3,2,5,1,3,4], [3,4], [1,1,2,3]]
#     outputs = [22, 12, -1]
#     sol = Solution()
#     for i in range(len(inputs)):
#         input = inputs[i]
#         output = outputs[i]
#
#         result = sol.dividePlayers(input)
#         if result != output:
#             return False
#
#     return True
#
# print(test())
