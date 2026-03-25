class Solution:
    def isOdd(self, n: int) -> bool:
        if (n % 2) !=0:
            return True 
        else:
            return False

#example code
n = 5
obj = Solution()    
print(obj.isOdd(n))