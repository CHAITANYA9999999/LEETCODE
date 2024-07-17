class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(set(s)) == 1:
            return 0
        if not s:
            return 0
        max_length = 0

        i=0
        n = len(s)
        while i<n:
            j=i
            open_bracket=0
            while j<n:
                if s[j] == "(":
                    open_bracket+=1
                else:
                    if not open_bracket:
                        break
                    else:
                        open_bracket-=1
                if not open_bracket:
                    max_length = max(max_length,j-i+1)
                j+=1
            i+=1
        return max_length
                