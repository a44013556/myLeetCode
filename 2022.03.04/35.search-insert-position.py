#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)
        nums = sorted(nums)
        return nums.index(target)

    def searchInsert2(self, nums: List[int], target: int) -> int:
        for i ,num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)
# @lc code=end

