class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        maxLength = start = 0
        for i, c in enumerate(s):
            if c in used and used[c] >= start:
                start = used[c] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            used[c] = i
        return maxLength
