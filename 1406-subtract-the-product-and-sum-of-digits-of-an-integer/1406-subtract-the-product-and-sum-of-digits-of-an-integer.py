class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        sums = 0
        mul = 1
        while temp > 0:
            digit = temp%10
            sums += digit
            mul *= digit
            temp //= 10
        return mul - sums