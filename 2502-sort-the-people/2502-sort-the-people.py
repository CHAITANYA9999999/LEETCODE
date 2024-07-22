class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [x for _,x in sorted(zip(heights,names),reverse = True)]