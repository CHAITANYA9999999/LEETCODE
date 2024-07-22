class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return reversed([x for _,x in sorted(zip(heights,names))])