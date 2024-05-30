class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # isme basically pehle ham har ek point se ek subarray dhoondenge jiss subarray ka xor 0 aa rha hoga fir uss subarray ki length add kar denge.. kyunki agar tum dekhoge to ki vo aapas me sab ek doosre ko cancel out kar rhe honge... to ham j ko i ke baad se k tak kahi par bhi rakh sakte hai... esiliye hamne count me (k-i) add kiya: for eg

#        p1                   p2
# [5, 6, 2, 3, 3, 5, 3, 2, 5, 3, 8, 9]
# Then the subarray looks like =[2, 3, 3, 5, 3, 2, 5, 3]. The XOR of this subarray is 0.
# If we look at above, the XOR from p1 to p2 will always be 0, because

# 2 will cut 2
# 3 will cut 3
# 5 will cut 5
# again, 3 will cut 3
# We have calculate the XOR, we going to put i at p1, k at p2

# And let's say we put j on 3, Now what will happen is, the 2, 3, 3, 5, 3, 2, 5, 3, will going to split to 2 - 3, 3, 5, 3, 2, 5, 3

# Now our X will have 2, because the X will be the value before the j i.e. X = i to j - 1
# And from j to k, we are having Y, i.e. 3, 3, 5, 3, 2, 5, 3
# And let's say we put j on 3, Now what will happen is, the 2, 3, 3, 5, 3, 2, 5, 3, will going to split to 2, 3 - 3, 5, 3, 2, 5, 3

# Now our X will have 2, 3, because the X will be the value before the j i.e. X = i to j - 1
# And from j to k, we are having Y, i.e. 3, 5, 3, 2, 5, 3
# And let's say we put j on 5, Now what will happen is, the 2, 3, 3, 5, 3, 2, 5, 3, will going to split to 2, 3, 3 - 5, 3, 2, 5, 3

# Now our X will have 2, 3, 3, because the X will be the value before the j i.e. X = i to j - 1
# And from j to k, we are having Y, i.e. 5, 3, 2, 5, 3
# And let's say we put j on 3, Now what will happen is, the 2, 3, 3, 5, 3, 2, 5, 3, will going to split to 2, 3, 3, 5 - 3, 2, 5, 3

# Now our X will have 2, 3, 3, 5, because the X will be the value before the j i.e. X = i to j - 1
# And from j to k, we are having Y, i.e. 3, 2, 5, 3
# And let's say we put j on 2, Now what will happen is, the 2, 3, 3, 5, 3, 2, 5, 3, will going to split to 2, 3, 3, 5, 3 - 2, 5, 3

# Now our X will have 2, 3, 3, 5, 3, because the X will be the value before the j i.e. X = i to j - 1
# And from j to k, we are having Y, i.e. 2, 5, 3
# And let's say we put j on 5, Now what will happen is, the 2, 3, 3, 5, 3, 2, 5, 3, will going to split to 2, 3, 3, 5, 3, 2 - 5, 3

# Now our X will have 2, 3, 3, 5, 3, 2, because the X will be the value before the j i.e. X = i to j - 1
# And from j to k, we are having Y, i.e. 5, 3
# And let's say we put j on 3, Now what will happen is, the 2, 3, 3, 5, 3, 2, 5, 3, will going to split to 2, 3, 3, 5, 3, 2, 5 - 3

# Now our X will have 2, 3, 3, 5, 3, 2, 5, because the X will be the value before the j i.e. X = i to j - 1
# And from j to k, we are having Y, i.e. 3
        count = 0
        
        for i in range(len(arr)):
            val = arr[i]
            
            for k in range(i + 1, len(arr)):
                val ^= arr[k]
                
                if val == 0:
                    count += (k - i)
        
        return count