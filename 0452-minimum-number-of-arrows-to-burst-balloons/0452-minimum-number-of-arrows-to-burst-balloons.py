class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = []
        i=1
        cur_left = points[0][0]
        cur_right = points[0][1]
        while i<len(points):
            left = points[i][0]
            right = points[i][1]
            if left>cur_right:
                res.append([left,right])
                cur_right = right
            else:
                cur_right = min(cur_right,right)
            cur_left = max(cur_left,left)
            print(cur_left, cur_right)
            i+=1
        return len(res)+1