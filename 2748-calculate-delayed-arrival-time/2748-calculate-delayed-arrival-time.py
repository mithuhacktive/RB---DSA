class Solution:
    def findDelayedArrivalTime(self, at: int, dt: int) -> int:
        a = at+dt
        if a == 24:
            return 0
        if a%24==0:
            return a
        return a%24