class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def isAnagram(s:str, t:str) -> bool:
            if len(s) != len(t):
                return False
            count_s = {}
            for c in s:
                count_s[c] = count_s.get(c,0) + 1
            
            for c in t:
                if c not in count_s:
                    return False
                count_s[c] -= 1
                if count_s[c] < 0:
                    return False
            return True
        
        if len(s1) > len(s2):
            return False
        win = len(s1) - 1
        l = 0
        while l + win < len(s2):
            if isAnagram(s1, s2[l:l+win+1]):
                return True
            l+=1
        return False
        