class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        presum = {0:0}

        for rod in rods:
            newsum = {}
            for val, pos_val in presum.items():
                newsum[val + rod] = max(newsum.get(val + rod, 0), pos_val + rod)
                newsum[val - rod] = max(newsum.get(val - rod, 0), pos_val)
                newsum[val] = max(newsum.get(val, 0), pos_val)
            presum = newsum
        return presum[0]