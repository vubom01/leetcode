# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/?envType=daily-question&envId=2024-10-04
from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        numberOfSkill = [0 for _ in range(2001)]
        for s in skill:
            numberOfSkill[s] += 1
        sumOfEachTeam = int(sum(skill) / (len(skill) / 2))
        result = 0
        for s in skill:
            if numberOfSkill[s] == 0:
                continue
            if numberOfSkill[sumOfEachTeam - s] == 0:
                return -1
            result += s * (sumOfEachTeam - s)
            numberOfSkill[s] -= 1
            numberOfSkill[sumOfEachTeam - s] -= 1

        return result

sol = Solution()
print(sol.dividePlayers([1, 1000]))


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