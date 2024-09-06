# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/?envType=daily-question&envId=2024-09-06

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        node = head
        while node is not None:
            while node.val in nums:
                node.val = node.next.val if node.next is not None else None
                node.next = node.next.next if node.next is not None else None
            node = node.next

        node = head
        while node.next is not None and node.next.val is not None:
            node = node.next
        node.next = None
        return head


sol = Solution()
print(sol.modifiedList(
    [1,1,2,3],
    ListNode(
        val=1,
        next=ListNode(
            val=2,
            next=ListNode(
                val=3,
                next=ListNode(
                    val=4,
                    next=ListNode(
                        val=5
                    )
                )
            )
        )
    ),
))