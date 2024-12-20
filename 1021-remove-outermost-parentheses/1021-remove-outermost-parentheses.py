class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st = ""
        counter = 0
        for i in range(len(s)):
            if s[i] == "(":
                if counter == 0:
                    counter += 1
                else:
                    counter += 1
                    st += "("
            else:
                counter -= 1
                if counter != 0:
                    st += ")"
        return st