class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mapp = {}
        for i in nums:
            mapp[i] = mapp.get(i, 0) + 1
        
        res = []
        for i,j in mapp.items():
            if j > len(nums)//3:
                res.append(i)
        return res