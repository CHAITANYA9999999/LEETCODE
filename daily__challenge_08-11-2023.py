class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        if sx==fx and sy==fy:
            return t!=1
        if t>=max(abs(fx-sx),abs(fy-sy)):
            return True
        return False
