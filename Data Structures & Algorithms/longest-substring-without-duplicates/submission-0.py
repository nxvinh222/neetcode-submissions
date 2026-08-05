class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mem = {}
        res = 0

        left = 0
        right = -1

        while right < len(s) - 1:
            right += 1
            if s[right] in mem and mem[s[right]] >= left:
                left = mem[s[right]] + 1
                
            res = max(right - left + 1, res)
            mem[s[right]] = right

        return res
        