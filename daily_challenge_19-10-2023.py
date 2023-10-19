class Solution(object):
    def backspaceCompare(self, s, t):
        stack1=[]
        stack2=[]
        i=0
        j=0
        while i<len(s) and j<len(t):
            if s[i]=='#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(s[i])
            i+=1

            if t[j]=='#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(t[j])
            j+=1
        while i<len(s):
            if s[i]=='#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(s[i])
            i+=1
        while j<len(t):
            if t[j]=='#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(t[j])
            j+=1
        return stack1==stack2