class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = 0
        mem = {}
        
        left = 0

        maxUpdate = 0

        res = 0

        for char in s:
            if char not in mem:
                mem[char] = 1
            else:
                mem[char] = mem[char] + 1

            maxUpdate = max(maxUpdate, mem[char])

            count += 1

            while count - maxUpdate > k:
                mem[s[left]] = mem[s[left]] - 1
                left += 1
                count -= 1
            
            res = max(res, count)

        return res
        