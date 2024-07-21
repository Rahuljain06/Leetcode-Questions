class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:

#1: ham basically isme consecutive elements ko check karenge agar consecutive elements ka diff(target[i]-nums[i]) ke value peechle diff se choti hai to ham use ignore kar denge and res me add nhi karenge but agar badi hai to add karenge.

#2: har baar ham peechle pos ki value ko apne curr diff value se update kar denge. jisse next wale element ka diff ham prev_diff(pos) se check kar paaye or 1st step repeat kar paaye..

# This is the special case: [1,5,2]
                        #   [10,6,11]
#Dry Run
# [1,5,2]
# [10,6,11]

# i=0 ke liye diff=9 aya and pichla diff 0 hai to hamne res+=9-0 kar diya [res=9]
# i=1 ke liye diff=1 aya and pichla diff 9 hai to add karne ki jaroorat nhi hai [res=9]
# i=2 ke liye diff=9 aya and pichla diff 1 hai to hamne res+=9-1 kar diya [res=17]
# and final ans 17 aya

        n = len(nums)
        pos, neg, res = 0, 0, 0
        for i in range(n):
            d=target[i] - nums[i]

            if d>0:
                if pos<d:
                    res+=d-pos
                pos=d
                neg=0
            elif d<0:
                if neg<-d:
                    res+=-d-neg
                neg=-d
                pos=0
            else:
                pos=0
                neg=0
        return res
       