"""
https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/description/
"""

"""
- For each i, "tìm tổng n số bé nhất từ 0->i, nếu có thể", "tìm tổng n số lớn nhất từ i + 1 đến 3*n, nếu có thể"
- Find the sum of the smallest n numbers from 0 to i, if possible
- Find the sum of the largest n numbers from i + 1 to 3 * n, if possible
- The result is the minimum of left[i] - right[i+1] for all i in range(n, 2*n)
- TC: O(3*n)
- SC: O(3*n)
"""

import heapq
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        total = 0
        heap = []
        left = []
        for i in range(3 * n):
            total += nums[i]
            heapq.heappush(heap, -nums[i])
            if len(heap) > n:
                total -= -heapq.heappop(heap)
            left.append(total)

        heap = []
        total = 0
        res = float('inf')
        for i in range(3 * n - 1, n - 1, -1):
            total += nums[i]
            heapq.heappush(heap, nums[i])
            if len(heap) > n:
                total -= heapq.heappop(heap)
            if len(heap) == n:
                res = min(res, left[i - 1] - total)

        return res


s = Solution()
print(s.minimumDifference([7, 9, 5, 8, 1, 3]))
