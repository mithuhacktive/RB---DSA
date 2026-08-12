class Solution:
    def sortColors(self, n: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(n)-1
        i = 0
        while i<=r:
            if n[i]==0:
                n[i] , n[l] = n[l] , n[i]
                i+=1
                l+=1
            elif n[i]==2:
                n[i] , n[r] = n[r] ,n[i]
                r-=1
            else:
                i+=1
        return n