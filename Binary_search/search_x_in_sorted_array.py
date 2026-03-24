class Solution:
    def search(self, nums, x):
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == x:
                return mid
            elif nums[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1  
#example code
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 5
obj = Solution()
print(obj.search(arr, x))