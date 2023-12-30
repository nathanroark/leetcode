from typing import List


# start at index 0 Solution
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        for i, n in enumerate(nums):
            right -= n
            if left == right:
                return i
            left += n
        return -1


# i spent a while on this attempting to do it starting from a middle index
# i think it's possible but it's not worth the amount of possible ways to make mistakes compared to the above solution
