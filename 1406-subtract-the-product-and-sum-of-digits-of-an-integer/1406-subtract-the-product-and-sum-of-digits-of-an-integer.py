class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sums = 0
        mul = 1
        while n > 0:
            digit = n%10
            sums += digit
            mul *= digit
            n //= 10
        return mul - sums