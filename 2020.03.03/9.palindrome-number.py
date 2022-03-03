#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return 0 if x < 0 else str(x) == str(x)[::-1]
# @lc code=end

