# https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/description/

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
