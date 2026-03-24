class Solution:
    def findPeakElement(self, arr):
        n=len(arr)
        if n==1 or arr[0] > arr[1]:
            return 0
        for i in range(1, n-1):
            if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
                return i

        if arr[n-1]>arr[n-2]:
            return n-1

#example code
arr = [1, 2, 3, 1]
obj = Solution()
print(obj.findPeakElement(arr))