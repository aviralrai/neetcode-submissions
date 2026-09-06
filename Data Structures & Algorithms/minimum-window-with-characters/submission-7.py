class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        curr = {}
        need = len(count_t)
        have = 0
        l = r = 0
        ans = (-1,-1)
        anslen = float("inf")
        while r < len(s):
            curr[s[r]] = curr.get(s[r],0) + 1
            if s[r] in count_t and curr[s[r]] == count_t[s[r]]:
                have += 1
            while have == need:
                if anslen > r-l+1:
                    ans = (l,r)
                    anslen = r-l+1
                curr[s[l]] -= 1
                if s[l] in count_t and curr[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
            r += 1
        l,r = ans
        return s[l:r+1] if anslen != float("inf") else ""