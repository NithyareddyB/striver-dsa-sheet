class Solution:
    def GCD(self, a, b):
        while b:
            a, b = b, a % b
        return a

# Example usage:
a = 48
b = 18  
obj = Solution()
print(obj.GCD(a, b))

#brute force approach
class Solution:         
    def GCD(self, a, b):
        gcd = 1
        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                gcd = i
        return gcd

# Example usage:    
a = 48
b = 18
obj = Solution()
print(obj.GCD(a, b))