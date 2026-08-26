class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = {}
        res = 0
        r = 0
        while r < len(s):
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1
            max_f = max(freq.values())
            if r-l+1 - max_f <= k:
                res = max(res,r-l+1)
                r+=1
            else:
                freq[s[l]] -= 1
                freq[s[r]] -= 1
                l += 1
        return res

            

        


                
                
        