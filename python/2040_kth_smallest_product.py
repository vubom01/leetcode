"""
https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/description/
"""

"""
- Binary search the result
- For each value, counter the number of pairs whose product of 2 numbers is less than it
- How to count the number of pairs?
--- Approach 1: Binary Search -> Time Limit Exceeded
    - For each index i1 in the nums1, find the largest index i2 in nums2 such that nums1[i1] * nums2[i2] <= val
    - TC: O(n * log m * log 2e10)
    - SC: O(1)
--- Approach 2: Two pointers
    - Use a pointer on nums1 and another on nums2, and handle negative and positive number cases separately
    - TC: O((n + m) log 2e10)
    - SC: O(1)
"""

from typing import List


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n1, n2 = len(nums1), len(nums2)
        pos1, pos2 = 0, 0
        while pos1 < n1 and nums1[pos1] < 0:
            pos1 += 1
        while pos2 < n2 and nums2[pos2] < 0:
            pos2 += 1

        left = -10000000000
        right = 10000000000
        res = right

        while left <= right:
            mid = (left + right) // 2
            counter = 0

            # negative - negative
            i1, i2 = 0, pos2 - 1
            while i1 < pos1 and i2 >= 0:
                if nums1[i1] * nums2[i2] > mid:
                    i1 += 1
                else:
                    counter += pos1 - i1
                    i2 -= 1

            # positive - positive
            i1, i2 = n1 - 1, pos2
            while i1 >= pos1 and i2 < n2:
                if nums1[i1] * nums2[i2] > mid:
                    i1 -= 1
                else:
                    counter += i1 - pos1 + 1
                    i2 += 1

            # positive - negative
            i1, i2 = n1 - 1, pos2 - 1
            while i1 >= pos1 and i2 >= 0:
                if nums1[i1] * nums2[i2] > mid:
                    i2 -= 1
                else:
                    counter += i2 + 1
                    i1 -= 1

            # negative - positive
            i1, i2 = pos1 - 1, n2 - 1
            while i1 >= 0 and i2 >= pos2:
                if nums1[i1] * nums2[i2] > mid:
                    i1 -= 1
                else:
                    counter += i1 + 1
                    i2 -= 1

            if counter >= k:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res


sol = Solution()
print(sol.kthSmallestProduct([-4, -2, 0, 3], [2, 4], 6))
print(sol.kthSmallestProduct([2, 5], [3, 4], 2))
print(sol.kthSmallestProduct([-2, -1, 0, 1, 2], [-3, -1, 2, 4, 5], 3))
print(sol.kthSmallestProduct([-9, 6, 10], [-7, -1, 1, 2, 3, 4, 4, 6, 9, 10], 15))
print(sol.kthSmallestProduct([-9, -4, 1, 6, 8, 8, 9, 10], [-10, -10, -8, -8, 1, 3, 6, 6, 8, 10], 29))
