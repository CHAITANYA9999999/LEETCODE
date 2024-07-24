class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            new_num = ""
            str_num = str(num)
            for i in range(len(str_num)):
                new_num += str(mapping[int(str_num[i])])
            res.append(int(new_num))
        print(res)
        return [num for _,_,num in sorted([[res[i],i,nums[i]] for i in range(len(nums))])]