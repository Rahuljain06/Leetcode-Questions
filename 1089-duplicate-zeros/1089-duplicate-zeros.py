class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        zeros = arr.count(0)
        nlen = n + zeros
        
        i = n - 1
        j = nlen - 1
        while i!=j:
            if j < n:
                arr[j] = arr[i]
            j-=1
            if arr[i] == 0:
                if j < n: arr[j] = arr[i]
                j -= 1
            i-=1