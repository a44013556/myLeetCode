#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, strs: str) -> int:
        dic = {}
        res = j = 0

        for i,s in enumerate(strs):
            if s in dic:
                # j is the latest index for s in the strs
                j = max(j,dic[s] + 1)
            # put the character's index in the dictionary
            dic[s] = i
            # the len is now index - the latest index for s which is repeating
            # +1 is for the strs which has no repeating characters
            res = max(res,i - j + 1)
        return res
# @lc code=end

