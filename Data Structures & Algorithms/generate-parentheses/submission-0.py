class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def rec(current,op,cl):
            if len(current) == 2 * n:
                ans.append(current)
            if op < n:
                rec(current+"(",op+1,cl)
            if cl < op:
                rec(current+")",op,cl+1)
            
        rec("",0,0)
        return ans

        