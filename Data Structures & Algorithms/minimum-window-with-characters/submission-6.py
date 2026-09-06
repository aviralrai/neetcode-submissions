class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        curr = {}
        need = len(count_t)
        have = 0
        l = r = 0
        ans = ""
        while r < len(s):
            curr[s[r]] = curr.get(s[r],0) + 1
            if s[r] in count_t and curr[s[r]] == count_t[s[r]]:
                have += 1
            while have == need:
                if len(ans) == 0 or len(ans) > r-l+1:
                    ans = s[l:r+1]
                curr[s[l]] -= 1
                if s[l] in count_t and curr[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
            r += 1
        return ans