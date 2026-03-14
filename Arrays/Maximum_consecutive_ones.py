class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        max_count = 0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                count = 0
            max_count = max(max_count, count)
        return max_count

# Example usage:
nums = [1, 1, 0, 1, 1, 1]
obj = Solution()
print(obj.findMaxConsecutiveOnes(nums))