class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count_s = {}
        for c in s1:
            count_s[c] = count_s.get(c, 0) + 1
        curr = {}
        win = len(s1)
        for c in s2[:win]:
            curr[c] = curr.get(c, 0) + 1
        for l in range(len(s2) - win + 1):
            if all(curr.get(k, 0) == count_s.get(k, 0) for k in count_s) and all(curr.get(k, 0) == count_s.get(k, 0) for k in curr):
                return True
            if l + win < len(s2):
                curr[s2[l + win]] = curr.get(s2[l + win], 0) + 1
                curr[s2[l]] -= 1
                if curr[s2[l]] == 0:
                    del curr[s2[l]]
        return False
