class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # so basically isme hame 0 index se i loop lagana hai and uske andar i+1 index se doosra kyunki ham -ve values consider nhi karenge... fir ek hashmap lekar usme (j index, nums[j]-nums[i]) ye values add karte jayenge and add karne se pehle check kar lenge ki i index se pehle to ye vaule nhi hai.agr hai to add kar denge warna (j index, nums[j]-nums[i])=2 se initialize karenge 2 se esiliye karenge 2 elements minium honge tabhi to airthmetic subsequence bangega
        
        d=defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                diff=nums[j]-nums[i]
                d[(j,diff)]=d.get((i,diff),1)+1
        return max(d.values())