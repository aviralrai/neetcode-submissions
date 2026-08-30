class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count = [0] * 26
        matches = 26
        m = len(s1)
        for c in s1:
            if count[ord(c)-ord('a')] == 0:
                matches -= 1
            count[ord(c)-ord('a')] -= 1
        for h in range(len(s2)):
            i = ord(s2[h])-ord('a')
            if count[i] == 0:
                matches -= 1
            count[i] += 1
            if count[i] == 0:
                matches += 1
            if h > m-1:
                l = ord(s2[h-m]) - ord('a')
                if count[l] == 0:
                    matches -= 1
                count[l] -= 1
                if count[l] == 0:
                    matches += 1
            print(matches)
            if matches == 26:
                return True
        return False