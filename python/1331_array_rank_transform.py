"""
https://leetcode.com/problems/rank-transform-of-an-array/description/
"""

from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(set(arr))
        rank_dict = {value: index + 1 for index, value in enumerate(sorted_unique)}
        return [rank_dict[value] for value in arr]


sol = Solution()
print(sol.arrayRankTransform([40, 10, 20, 30]))
