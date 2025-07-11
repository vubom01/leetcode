"""
https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/description/
"""

"""
- Let k = 2 ^ i + t
- The k-th character is calculated based on the t-th character after i operations
- Find the largest i such that k > 2 ^ i
- Update k to k - 2 ^ i. If operations[i] = 1, increase the result by 1
- TC: O(n) (can be optimize to log k)
- SC: O(1)
"""

from typing import List


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        cnt = 0
        for i in range(len(operations) - 1, -1, -1):
            if k > 2 ** i:
                k -= 2 ** i
                if operations[i]:
                    cnt += 1
        return chr(ord('a') + cnt % 26)


s = Solution()
print(s.kthCharacter(15, [0, 1, 0, 1]))
