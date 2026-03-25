class Solution:
    def fib(self, n):
        if n==0 or n==1:
            return n
        else:
            return self.fib(n-1)+self.fib(n-2)


#example code
n = 5                       
obj = Solution()
print(obj.fib(n))