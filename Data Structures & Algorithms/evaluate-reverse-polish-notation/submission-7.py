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
                    ans = int(x)+int(y)
                elif ele == "-":
                    ans = int(x)-int(y)
                elif ele == "*":
                    ans = int(x)*int(y)
                else:
                    ans = int(x)/int(y)
                    ans = int(ans)
                stack.append(ans)
                print(ans)
            else:
                stack.append(int(ele))
        return stack[-1]
        