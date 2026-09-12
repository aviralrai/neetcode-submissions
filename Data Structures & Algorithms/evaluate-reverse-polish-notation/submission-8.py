class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ("+","-","*","/")
        stack = []
        for ele in tokens:
            if ele in operators:
                y = stack.pop()
                x = stack.pop()
                ans = 0
                if ele == "+":
                    ans = x+y
                elif ele == "-":
                    ans = x-y
                elif ele == "*":
                    ans = x*y
                else:
                    ans = x/y
                    ans = int(ans)
                stack.append(ans)
            else:
                stack.append(int(ele))
        return stack[-1]
        