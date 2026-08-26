class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        countT = {}
        for i in t:
            if i in countT:
                countT[i] += 1
            else:
                countT[i] = 1
        def checkValid(countS1,countT):
            for key,val in countT.items():
                if key not in countS1:
                    return False
                elif val > countS1[key]:
                    return False
            return True
        l = 0
        countS1 = {}
        ans = ""
        for r in range(len(s)): 
            if s[r] in countS1:
                countS1[s[r]] += 1
            else:
                countS1[s[r]] = 1 
            if checkValid(countS1,countT):
                print(s[l:r+1])
                for i in range(l,r+1):
                    countS1[s[i]] -= 1
                    if not checkValid(countS1,countT):
                        print(s[i:r+1])
                        if ans == "":
                            ans = s[i:r+1]
                        elif len(ans) > r-i+1:
                            ans = s[i:r+1]
                        # countS1[s[i]] += 1
                        l = i+1
                        break
                
        # first = -1
        # for l in range(last+1):
        #     countS1[s[l]] -= 1
        #     if not checkValid(countS1,countT):
        #         first = l
        #         break
        return ans
        