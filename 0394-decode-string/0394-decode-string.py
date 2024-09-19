class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                temp = ""
                while stack and stack[-1] != "[":
                    temp = stack.pop() + temp
                stack.pop()
                no = ""
                while stack and stack[-1].isdigit():
                    no = stack.pop() + no
                stack.append(int(no) * temp)
        return "".join(stack)