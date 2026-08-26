class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sub = set()

        max_len = 0
        for i in range(len(s)):
            while s[i] in sub:
                sub.remove(s[l])
                l+=1
            sub.add(s[i])
            max_len = max(max_len,i-l+1)
        return max_len
                

        