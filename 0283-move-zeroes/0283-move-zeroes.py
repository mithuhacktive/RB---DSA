class Solution:
    def moveZeroes(self, num: List[int]) -> None:
        zero = []
        cons = []
        for i in num:
            if i == 0:
                zero.append(i)
            else:
                cons.append(i)
        num[:] = cons + zero