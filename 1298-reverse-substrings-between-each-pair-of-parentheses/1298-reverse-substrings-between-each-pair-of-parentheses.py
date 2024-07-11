class Solution:
    def reverseParentheses(self, s: str) -> str:
        l = []
        for ch in s:
            if ch!=')':
                l.append(ch)
            else:
                temp = []
                while l[-1]!='(':
                    temp.append(l.pop())
                l.pop()
                l.extend(temp)
        return ''.join(l)