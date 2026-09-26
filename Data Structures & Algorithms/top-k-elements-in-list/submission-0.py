class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        map = {}

        for i in nums:
            map[i] =  map.get(i, 0) + 1
        
        map = sorted(map.items(), key = lambda x:x[1], reverse = True)

        res = []
        for i in range(k):
            res.append(map[i][0])
        return res

        