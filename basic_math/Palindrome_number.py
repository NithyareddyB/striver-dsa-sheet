class Solution:
    def isPalindrome(self, n):
        rev = 0
        temp = n
        while temp > 0:
            last = temp % 10
            rev = rev * 10 + last
            temp //= 10
        return rev == n

# Example usage:    
n = 121 
obj = Solution()
print(obj.isPalindrome(n))
n=1234
print(obj.isPalindrome(n))