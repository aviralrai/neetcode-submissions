class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_s = {}
        freq_t = {}
        for i in range(len(s)):
            if s[i] in freq_s.keys():
                freq_s[s[i]] += 1
            else:
                freq_s[s[i]] = 1
            if t[i] in freq_t.keys():
                freq_t[t[i]] += 1
            else:
                freq_t[t[i]] = 1
        return freq_s == freq_t
        