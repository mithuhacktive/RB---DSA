class Solution:
    def maximumWealth(self, a: List[List[int]]) -> int:
        m = 0
        for i in range(len(a)):
            w = sum(a[i])
            m = max(m,w)
        return m
