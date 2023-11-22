class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        dic={}
        ans=[]
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i+j not in dic:
                    dic[i+j]=[nums[i][j]]
                else:
                    dic[i+j].append(nums[i][j])
        for i in dic.keys():
            # ans.extend(list(reversed(dic[i])))
            ans.extend(dic[i][::-1])
        return ans
