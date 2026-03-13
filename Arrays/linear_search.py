class Solution:
    def linearSearch(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
               return i
        return -1 
# Example usage:
nums = [3, 1, 4, 1, 5, 9]
target = 5
obj = Solution()
print(obj.linearSearch(nums, target))