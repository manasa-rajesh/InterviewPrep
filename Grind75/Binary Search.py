class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(arr, low, high, x):
            if high>=low:
                mid = (high + low) // 2
                
                if arr[mid] == x:
                    return mid
                if arr[mid] > x:
                    return binarySearch(arr, low, mid-1, x)
                if arr[mid] < x:
                    return binarySearch(arr, mid+1, high,x)
            else:
                return -1
            
        return binarySearch(nums, 0, len(nums)-1, target)