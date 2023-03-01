class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)
    
    
    
    def merge_sort(self,arr):

        if len(arr)==1:
            return arr

        mid=len(arr)//2

        left_value=self.merge_sort(arr[:mid])  
        right_value=self.merge_sort(arr[mid:])

        sorted_values=[]
        l=0
        r=0

        while l<len(left_value) and r<len(right_value):
            if left_value[l]<right_value[r]:
                sorted_values.append(left_value[l])
                l+=1
            else:
                sorted_values.append(right_value[r])
                r+=1

        sorted_values+=left_value[l:]
        sorted_values+=right_value[r:]
        return sorted_values
