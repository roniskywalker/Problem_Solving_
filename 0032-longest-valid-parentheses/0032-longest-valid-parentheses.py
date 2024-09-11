class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = max_length = 0
        for i in s:
            if i == "(":
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, left + right)
            elif right > left:
                left = right = 0
        left = right = 0
        for i in s[::-1]:
            if i == "(":
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, left + right)
            elif right < left:
                left = right = 0
        return max_length