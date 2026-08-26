class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new = ''.join(s.split(" "))
        l = 0
        r = len(new)-1
        while l < r:
            # print(new[l],new[r])
            if not new[l].isalnum():
                l+=1
                continue
            if not new[r].isalnum():
                r-=1
                continue
            if new[l] == new[r]:
                l+=1
                r-=1
            else:
                return False
        return True
            

        