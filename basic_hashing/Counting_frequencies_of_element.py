class Solution:
    def countFrequencies(self, nums):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        result = []
        for key, value in freq.items():
            result.append([key, value])

        return result
#example code
arr = [1, 2, 2, 3, 3, 3, 4]
obj = Solution()
print(obj.countFrequencies(arr))