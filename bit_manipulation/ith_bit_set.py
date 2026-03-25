class Solution:
    def checkIthBit(self, n: int, i: int) -> bool:
        return ((n>>i)&1)==1

#example code
n = 5
i = 0
obj = Solution()    
print(obj.checkIthBit(n, i))