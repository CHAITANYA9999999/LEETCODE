class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row=[[1],[1,1]]
        if rowIndex<2:
            return row[rowIndex]
        row=[1,1]
        for i in range(3,rowIndex+2):
            temp=[1]
            for j in range(1,(i+1)//2):
                temp.append(row[j]+row[j-1])
            if i%2:
                temp=temp+temp[:-1][::-1]
            else:
                temp=temp+temp[::-1]
            row=temp
        return row