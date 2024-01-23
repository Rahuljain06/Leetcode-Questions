class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # ham isme pehle uniqElements me ek empty string daal rhe hai jisse hamara neeche wala loop chale or fir ham ek arr[i] ko add kar rhe hai har baar unique elements list me jo values hai agar add karke bhi unique ban rha hai to maximum size store kar rhe hai.
        uniqELements = ['']
        maximum = 0
        for i in range(len(arr)):
            sz = len(uniqELements)
            for j in range(sz):
                x=arr[i]+uniqELements[j]
                if (len(x)==len(set(x))):
                    uniqELements.append(x)
                    maximum = max(maximum,len(x))
        #print(uniqELements)
        return maximum