class Solution:
    def threeSum(self, num: List[int]) -> List[List[int]]:
        num.sort()
        hashmap=set()
        for i in range(len(num) - 2):
            l, r = i+1, len(num) - 1
            while l < r:
                sum= num[i] + num[l] + num[r] 

                if sum >0:
                    r-=1
                elif sum<0:
                    l+=1
                else:
                    hashmap.add((num[i],num[l],num[r]))
                    l+=1
                    r-=1
            

        return hashmap