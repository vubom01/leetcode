"""
https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/description/
"""

"""
- DP
- For each x in range(0, k), dp[i] is the length of the longest subarray ending at nums[i]
  such that (nums[i - 1] + nums[i]) % k = x
- dp[i] = max(dp[j] + 1) for all 0 <= j < i such that (nums[j] + nums[i]) % k = x
- To find max(dp[j]), we only need to find the largest index j
- TC: O(n * k)
- SC: O(n * k)
"""

from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for x in range(k):
            prev = [-1] * k
            dp = [0] * n
            for i in range(n):
                num = nums[i] % k
                j = (x - num) % k
                if prev[j] != -1:
                    dp[i] = dp[prev[j]] + 1
                prev[num] = i
            res = max(res, max(dp) + 1)

        return res


s = Solution()
print(s.maximumLength([1, 4, 2, 3, 1, 4], 3))
