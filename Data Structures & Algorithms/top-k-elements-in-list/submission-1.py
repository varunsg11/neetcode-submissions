class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        mapp = {}
        
        for i in nums:
            mapp[i] = mapp.get(i, 0) + 1
        
        mapp = sorted(mapp.items(), key = lambda x:x[1], reverse = True)

        res = []
        for i in range(k):
            res.append(mapp[i][0])
        
        return res
        