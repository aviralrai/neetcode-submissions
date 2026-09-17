class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        set_s = set(s)
        di = {}
        for x in s:
            for i in range(len(s)):
                if s[i] == x:
                    if x in di:
                        prev,_ = di[x]
                        di[x] = [prev,i]
                    else:
                        di[x] = [i,i]
        inv = list(di.values())
        inv.sort()
        ans = []
        st,last = inv[0]
        for iv in inv[1:]:
            if last < iv[0]:
                ans.append(last - st + 1)
                st,last = iv
            else:
                last = max(last, iv[1])
        ans.append(last-st+1)
        return ans

        