# https://leetcode.com/problems/find-missing-observations/description/?envType=daily-question&envId=2024-09-05

from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean * (len(rolls) + n) - sum(rolls)
        medium_value = total / n

        if medium_value > 6 or medium_value < 1:
            return []

        medium_value = int(medium_value)

        result = [medium_value for _ in range(n)]
        sum_result = sum(result)
        index = 0
        while sum_result < total:
            result[index] += 1
            sum_result += 1
            index += 1
        return result

sol = Solution()
print(sol.missingRolls([6,1,5,2], 4, 4))