class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path, res = [], []
        def go(o, c):
            if len(path) == 2*n:
                res.append(''.join(path))
            if o < n:
                path.append("(")
                go(o+1,c)
                path.pop()
            if c < o:
                path.append(")")
                go(o,c+1)
                path.pop()
        go(0,0)
        return res
        