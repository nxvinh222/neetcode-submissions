class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        remaining = len(s1)

        left = 0

        mem = {}

        for char in s1:
            mem[char] = mem.get(char, 0) + 1

        for start in range(len(s2)):
            if s2[start] in mem:
                left = start
                break

        start = left
        for right in range(start, len(s2)):
            if s2[right] in mem:
                if mem[s2[right]] == 0:
                    while s2[left] != s2[right]:
                        mem[s2[left]] = mem[s2[left]] + 1
                        left += 1
                        remaining += 1
                    left += 1
                    continue
                mem[s2[right]] -= 1
                remaining -= 1
                if remaining == 0:
                    return True
            else:
                while left != right:
                    mem[s2[left]] =  mem[s2[left]] + 1
                    remaining += 1
                    left += 1
                left += 1

        return False
        