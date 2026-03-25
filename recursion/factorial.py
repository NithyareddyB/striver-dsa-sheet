class Solution:
    def factorial(self, n):
        if n==0:
            return 1
        
        return n*self.factorial(n-1)

#example code
n = 5
obj = Solution()
print(obj.factorial(n))