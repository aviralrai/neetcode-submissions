class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_s = set()
        l = 0
        r = 0
        max_l = 0
        while l <= r and r < len(s):
            while r < len(s) and s[r] not in sub_s:
                sub_s.add(s[r])
                r+=1
                max_l = max(len(sub_s),max_l)
            while r < len(s) and s[r] in sub_s:
                sub_s.remove(s[l])
                l+=1
        return max_l
        
        