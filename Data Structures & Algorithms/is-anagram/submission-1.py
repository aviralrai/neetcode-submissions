class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        has_s,has_t = dict(), dict()
        if len(s) != len(t):
            return False
        for i in s:
            if i in has_s.keys():
                has_s[i] += 1
            else:
                has_s[i] = 1
        for j in t:
            if j in has_t.keys():
                has_t[j] += 1
            else:
                has_t[j] = 1
        for i in has_t.keys():
            if i not in has_s.keys() or has_s[i] != has_t[i]:
                return False
        return True
