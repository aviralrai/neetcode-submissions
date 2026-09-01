class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charset = set(s)
        max_s = 0
        for c in charset:
            curr = {}
            l = 0
            r = 0
            while r < len(s):
                curr[s[r]] = curr.get(s[r],0) + 1
                if r-l+1 - curr.get(c,0) <= k:
                    max_s = max(max_s,r-l+1)
                    r += 1
                else:
                    curr[s[l]] -= 1
                    l += 1
        return max_s

                    
        