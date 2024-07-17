class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        rows = [[] for _ in range(numRows)]
        cur_row = 0
        inc=True
        for ch in s:
            print(cur_row)
            rows[cur_row].append(ch)
            if inc:
                cur_row+=1
            else:
                cur_row-=1
            if cur_row==0:
                inc = True
            elif cur_row == numRows-1:
                inc = False
        return ''.join([''.join(l) for l in rows])