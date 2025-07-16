"""
https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/description/
"""

"""
- Find the length of the longest alternating even-odd sequence
- Find the length of the longest odd-number sequence
- Find the length of the longest even-number sequence
- TC: O(n)
- SC: O(1)
"""

from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even = 0
        odd = 0

        even1 = 0
        odd1 = 0
        for num in nums:
            if num & 1:
                even = odd + 1
                even1 += 1
            else:
                odd = even + 1
                odd1 += 1
        return max(max(even, odd), max(even1, odd1))


s = Solution()
print(s.maximumLength(nums=[1, 2, 3, 4, 5]))
