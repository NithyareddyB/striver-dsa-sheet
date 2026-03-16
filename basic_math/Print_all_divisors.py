import math

class Solution:
    def printDivisors(self, n):
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                print(i)

                if i != n // i:
                    print(n // i)

n = 24
obj = Solution()
obj.printDivisors(n)