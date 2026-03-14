class Solution:
    def missingNumber(self, nums):
        n = len(nums) #if the numbers are from 1-n then len(nums)+1 since one number is missing 
        expected_sum = n*(n+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

# Example usage:
nums = [0,1, 2, 4, 5]         
obj = Solution()
print(obj.missingNumber(nums))