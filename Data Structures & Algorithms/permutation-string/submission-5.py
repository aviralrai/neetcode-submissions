class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count_s1 = {}
        for c in s1:
            count_s1[c] = count_s1.get(c,0) + 1
        m = len(s1)
        l = 0
        h = m
        curr = {}
        for c in s2[:m]:
            curr[c] = curr.get(c,0) + 1
        if curr == count_s1:
            return True
        while h < len(s2):
            curr[s2[l]] -= 1
            if curr[s2[l]] == 0:
                del curr[s2[l]]
            curr[s2[h]] = curr.get(s2[h],0) + 1
            l += 1
            h += 1
            if curr == count_s1:
                return True
        return False
