class Solution:
    def isArmstrong(self, n):
        sum = 0
        temp = n
        while temp > 0:
            last = temp % 10
            sum += last ** 3
            temp //= 10
        return sum == n

# Example usage:    
n = 153
obj = Solution()
print(obj.isArmstrong(n))   