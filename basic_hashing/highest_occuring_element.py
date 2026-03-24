class Solution:
    def mostFrequentElement(self, nums):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        max_freq = 0
        answer = float('inf')  
        for num, count in freq.items():
            if count > max_freq:
                max_freq=count
                answer = num

            elif count == max_freq:
                answer = min(answer,num) 
        
        return answer
     
#example code
arr = [1, 2, 2, 3, 3, 3, 4]
obj = Solution()
print(obj.mostFrequentElement(arr))