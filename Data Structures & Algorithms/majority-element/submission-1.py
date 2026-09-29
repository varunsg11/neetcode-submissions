class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maps = {}

        res, top = 0, 0

        for i in nums:
            maps[i] = maps.get(i, 0) + 1

            if top < maps[i]:
                res = i
                top = maps[i]
        return res