class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        curr = {}
        maxcnt = 0
        while r < len(s):
            curr[s[r]] = curr.get(s[r],0) + 1
            max_c = max(curr.values())
            while l < r and r-l+1 - max_c > k:
                curr[s[l]] -= 1
                l += 1 
            maxcnt = max(maxcnt,r-l+1)
            r += 1
        return maxcnt