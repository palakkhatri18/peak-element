#Given an 0-indexed array of integers arr[] of size n, find its peak element. An element is considered to be peak if it's value is greater than or equal to the values of its adjacent elements (if they exist).

#Note: The output will be 1 if the index returned by your function is correct; otherwise, it will be 0
class Solution:   
    def peakElement(self,arr, n):
        # Code here
        
            if n==1:
                return 0
            if arr[n-1]>arr[n-2]:
                return n-1
            else:
                for i in range(n):
                    if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
                        return i
                retrun -1