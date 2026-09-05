class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        curr = defaultdict(int)
        l = res = maxCount = 0
        for r, c in enumerate(s):
            curr[c] += 1
            maxCount = max(maxCount, curr[c])

            if r-l+1 - maxCount > k:
                curr[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        return res