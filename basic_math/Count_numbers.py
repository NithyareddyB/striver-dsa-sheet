class Solution:
    def countDigit(self, n):
        count =0
        while n>0:
            n//=10
            count+=1
        return count 

# Example usage:
n = 12345   
obj = Solution()
print(obj.countDigit(n))