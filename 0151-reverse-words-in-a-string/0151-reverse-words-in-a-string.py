class Solution:
    def reverseWords(self, s: str) -> str:
        final = ""
        i, m = 0, len(s)
        while i < m:
            if s[i] == " ":
                i += 1
            else:
                j = i + 1
                while j < m  and s[j] != " ":
                    j += 1
                temp = s[i:j]
                if final == "":
                    final += temp
                else:
                    final = temp + " " + final
                i = j + 1
        return final