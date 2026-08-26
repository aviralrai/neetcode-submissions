class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "[" or i =="{":
                stack.append(i)
                continue
            if i == ")" :
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            if i == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False 
            if i == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        # print(stack)
        if len(stack) == 0:
            return True
        else:
            return False


        