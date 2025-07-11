"""
https://leetcode.com/problems/find-missing-observations/description/
"""

"""
- Find the integer value of the average of the missing array
- Add 1 to the count of elements that are equal to the missing value
- TC: O(n)
- SC: O(n)
"""

from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean * (len(rolls) + n) - sum(rolls)
        medium_value = total / n

        if medium_value > 6 or medium_value < 1:
            return []

        medium_value = int(medium_value)
        missing = total - medium_value * n
        return [medium_value + 1] * missing + [medium_value] * (n - missing)


sol = Solution()
print(sol.missingRolls([1, 5, 6], 3, 4))
