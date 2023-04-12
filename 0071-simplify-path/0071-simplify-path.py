class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        skip=("..",".","")
        for c in path.split("/"):
            if stack and c == "..":
                stack.pop()
            elif c not in skip:
                stack.append(c)
        return "/"+"/".join(stack)