class Solution:
    def reverseNumber(self, n):
        rev = 0
        while n > 0:
            last = n % 10
            rev = rev * 10 + last
            n //= 10
        return rev

# Example usage:    
n = 153
obj = Solution()
print(obj.reverseNumber(n))