class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charset = set(s)
        max_s = 0
        for c in charset:
            cnt = l = 0
            for r, ch in enumerate(s):
                cnt += (ch == c)
                while r-l+1 - cnt > k:
                    cnt -= (s[l] == c)
                    l += 1
                max_s = max(max_s, r-l+1)
        return max_s