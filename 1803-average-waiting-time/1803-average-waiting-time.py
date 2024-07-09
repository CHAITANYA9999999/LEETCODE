class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cur_time = 0
        waiting = 0
        for arr,time in customers:
            if cur_time < arr:
                cur_time = arr
            cur_time += time
            waiting += (cur_time - arr)
        return waiting/len(customers)