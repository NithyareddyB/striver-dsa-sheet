class Solution:
    def isSorted(self, nums):
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                return False
        return True

# Example usage:
nums = [1, 2, 3, 4, 5]
obj = Solution()
print(obj.isSorted(nums))
nums = [5, 4, 3, 2, 1]
print(obj.isSorted(nums))
nums = [1, 3, 2, 4, 5]
print(obj.isSorted(nums))