class Solution:
    def secondLargestElement(self, nums):
        if len(nums) < 2:
            return -1
        largest = float('-inf')
        second_largest = float('-inf')
        for num in nums:
            if num > largest :
                second_largest = largest
                largest = num
            elif num > second_largest and num!=largest:
                second_largest = num
        if second_largest == float('-inf'):
            return -1
        
        return second_largest

# Example usage:
nums = [3, 1, 4, 1, 5, 9]
obj = Solution()
print(obj.secondLargestElement(nums))