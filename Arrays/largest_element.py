class Solution:
    def largestElement(self, nums):
        largest = nums[0]
        for num in nums:
            if num > largest:
                largest = num
        return largest

# Example usage:
nums = [3, 1, 4, 1, 5, 9]
obj = Solution()
print(obj.largestElement(nums))  # Output: 9